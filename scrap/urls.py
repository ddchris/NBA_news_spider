# -*- coding: utf-8 -*-
"""scraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from myapp import views


router = DefaultRouter()
router.register(r'myapp', views.Hot_NewsViewSet)

# 用 views.Hot_NewsViewSet 註冊網址的 router為 myapp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.scraping),
    url(r'^(\d+)/$', views.detail),
    # 值接帶參數時, 前面無須斜線
    url(r'^api/', include(router.urls)),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]