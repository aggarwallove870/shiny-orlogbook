# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change_password",change_password, name='change_password'),
    path("delete_user",delete_user, name='delete_user')
]
