# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.command.upload import upload
from django.db import models
from django.conf import settings

# Create your models here.


class Graphs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='csv_files',)

    def __str__(self):
        return self.user.username

class Institution(models.Model):

    institute = models.CharField(max_length = 200)

    def __str__(self):
        return self.institute


class Supervisor(models.Model):

    username = models.CharField(max_length = 200, verbose_name="username")
    institute = models.ForeignKey(Institution ,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.username


