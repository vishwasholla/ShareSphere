# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import random

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os

from core import settings


# Create your models here.

def upload_resume(self,filename):
    filename = str(filename).replace('\t','_')
    return f'resume/{self.user.username}/{filename}'

def upload_internship_certificate(self,filename):
    filename = str(filename).replace('\t', '_')
    return f'internship_certificate/{self.user.username}/{filename}'

def upload_courses_completed(self,filename):
    filename = str(filename).replace('\t', '_')
    return f'courses_completed/{self.user.username}/{filename}'

def upload_other_certificate(self,filename):
    filename = str(filename).replace('\t', '_')
    return f'other_certificate/{self.user.username}/{filename}'



class Media(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])],
                             upload_to=upload_resume)
    internship_certificate = models.FileField(blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])],
                             upload_to=upload_internship_certificate)
    courses_completed = models.FileField(blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])],
                             upload_to=upload_courses_completed)
    other_certificate = models.FileField(blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])],
                             upload_to=upload_other_certificate)
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='shared_user')

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return str(f'{self.user.username}_{self.id}')