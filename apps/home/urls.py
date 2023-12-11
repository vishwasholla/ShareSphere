# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('index', views.index, name='index'),
    path('', views.dashboard, name='home'),
    path('files', views.upload_files, name='files'),
    path('view_files_list', views.view_files_list, name='view_files_list'),
    path('view_files/<path:url>', views.view_files, name='view_files'),
    path('view_profile/<int:pk>', views.view_profile, name='view_profile'),
    path('share_files/<int:pk>', views.share_files, name='share_files'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
