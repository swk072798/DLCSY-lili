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
from django.urls import path, include
from sign_up import views as sign_up_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # path("../go_to_download",down_views.go_to_download),
    path("",include("download_res.urls")),
    path("", include("login.urls")),
    path("", include("sign_up.urls")),
    path("",include("join_team.urls")),
    # path("go_to_personal",sign_up_views.personal_page_select),
    path('',include("login.urls")),
    path("I_N/",include("Info_news.urls")),
    path('captcha/', include('captcha.urls')),

]
