"""DLCSY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('login',views.login_action.index),
    path('login_check',views.login_action.check_psw),
    path('register_sub',views.login_action.register_username),
    path('register',views.login_action.goto_register),
    path('send_message',views.send_message),
    path('check_code',views.check_code),
    # path('welcome',views.welcome.welcome),
    # path('logined_main',views.welcome.back_to_main),
    path('welcome1',views.welcome1),
    path('goto_forget_psw',views.goto_forget_psw),
    path('forget_psw_f',views.forget_psw_f),
    path('forget_psw_s',views.forget_psw_s),
    path('contact_me_1',views.contact_me_1),
    path('contact_me_2',views.contact_me_2),
    # path('produce_png',views.verifycode),
    path('refresh_captcha/', views.refresh_captcha),
    path('send_phone_message',views.send_phone_message,name='send_phone_message'),

]
