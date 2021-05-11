"""DjangoBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from BackendApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/signup/', views.add_user),
    path('api/auth/signin/', views.get_user),
    path('api/add/subject', views.add_subject),
    path('api/add/teacher', views.add_teacher),
    path('api/add/classroom', views.add_classroom),
    path('api/add/class', views.add_class),
    path('api/get/all/subjects', views.get_subjects),
    path('api/get/all/teachers', views.get_teachers)
]
