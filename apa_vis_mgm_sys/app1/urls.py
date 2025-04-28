"""
URL configuration for apa_vis_mgm_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('', loginpage,name='login'),
    path('index/', homepage,name='index'),
    path('add_visitor/', visitor_form,name='add_visitor'),
    path('add_pass/', pass_form,name='pass_form'),
    path('manage_visitor/',manage_visitor,name='manage_visitor'),
    path('manage_visitor/delete/<int:id>',delete_visitor,name='visitor_delete'), 
    path('manage_visitor/update/<int:id>',update_visitor,name='update_visitor'),   
    path('manage_pass/',manage_pass,name='manage_pass'),
    path('manage_pass/delete/<int:id>',delete_pass,name='delete_pass'),
    path('search_visitor/',search_visitor,name='search_visitor'),
    path('search_pass/',search_pass,name='search_pass'), 
    path('visitor_report/',visitor_report,name='visitor_report'),
    path('pass_report/',pass_report,name='pass_report'),
    path('manage_pass/pass_details/<int:id>',pass_details,name='pass_details'),
    path('logout/',user_logout,name='logout'),
]
