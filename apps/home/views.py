# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os.path

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User

from apps.home.forms import FileForm
from apps.home.models import Media
from core.settings import CORE_DIR


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard(request):
    users = User.objects.exclude(id=request.user.id).values()
    context = {'segment': 'dashboard','users':users}
    return render(request,'home/dashboard.html',context)

@login_required(login_url="/login/")
def upload_files(request):
    form = FileForm()
    context = {'segment': 'files','form':form}
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            resume = form.cleaned_data['resume']
            internship_certificate = form.cleaned_data['internship_certificate']
            courses_completed = form.cleaned_data['courses_completed']
            other_certificate = form.cleaned_data['other_certificate']
            media = Media(resume=resume,internship_certificate=internship_certificate,courses_completed=courses_completed,
                                 other_certificate=other_certificate,user_id=request.user.id,shared_user=request.user)
            media.save()
            return redirect('home')
    return render(request, 'home/files.html', context)

@login_required(login_url="/login/")
def view_files_list(request):
    if request.method == 'GET':
        media = Media.objects.filter(user_id=request.user.id).values()
        shared_media = Media.objects.filter(user_id=request.user.id).exclude(shared_user=request.user).values('shared_user__username','resume','other_certificate',
                                                                            'internship_certificate','courses_completed')
        context = {'segment': 'view_files_list','media':media,'shared_media':shared_media}
        return render(request, 'home/view_files.html', context)

@login_required(login_url="/login/")
def view_files(request,url):
    try:
        loc = os.path.join(CORE_DIR,f'apps/static/media/{url}')
        return FileResponse(open(loc, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

@login_required(login_url="/login/")
def view_profile(request,pk):
    print(pk)
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        context = {'user':user}
        return render(request,'home/view_profile.html',context)

@login_required(login_url="/login/")
def share_files(request,pk):
    media = Media.objects.filter(user_id=request.user.id).values()
    context = {'media':media,'pk':pk}
    if request.method == 'POST':
        print(request.POST)
        shared_files = request.POST.copy()
        del shared_files['csrfmiddlewaretoken']
        print(dict(shared_files).items())
        for key,value in dict(shared_files).items():
            print(f'key:{key},:{value}')
            media = Media(user_id=pk,shared_user=request.user)
            for file in value:
                dir = str(file).split('/')[0]
                print(f'dir:{dir}')
                if dir == 'resume':
                    media.resume = file
                elif dir == 'internship_certificate':
                    media.internship_certificate = file
                elif dir == 'other_certificate':
                    media.other_certificate = file
                elif dir == 'courses_completed':
                    media.courses_completed = file
            media.save()
        return render(request, 'home/share_files.html', context)
    return render(request, 'home/share_files.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
