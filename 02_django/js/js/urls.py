"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView

from js import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('js01', TemplateView.as_view(template_name='js01.html'), name='js01'),
    path('js02', TemplateView.as_view(template_name='js02.html'), name='js02'),
    path('js03', TemplateView.as_view(template_name='js03.html'), name='js03'),
    path('js04', TemplateView.as_view(template_name='js04.html'), name='js04'),
    path('js05', TemplateView.as_view(template_name='js05.html'), name='js05'),
    path('js06', TemplateView.as_view(template_name='js06.html'), name='js06'),
    path('js07', TemplateView.as_view(template_name='js07.html'), name='js07'),
    path('jq01', TemplateView.as_view(template_name='jq01.html'), name='jq01'),
    path('jq02', TemplateView.as_view(template_name='jq02.html'), name='jq02'),
    path('jq03', TemplateView.as_view(template_name='jq03.html'), name='jq03'),
    path('jq04', TemplateView.as_view(template_name='jq04.html'), name='jq04'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('jq05', TemplateView.as_view(template_name='jq05.html'), name='jq05'),
    path('registerimpl', views.registerimpl, name='registerimpl'),
    path('jq06', TemplateView.as_view(template_name='jq06.html'), name='jq06'),
    path('jq07', TemplateView.as_view(template_name='jq07.html'), name='jq07'),
    path('jq08', TemplateView.as_view(template_name='jq08.html'), name='jq08'),

    path('aj01', TemplateView.as_view(template_name='aj01.html'), name='aj01'),
    path('aj011', TemplateView.as_view(template_name='aj011.html'), name='aj011'),
    path('aj02', TemplateView.as_view(template_name='aj02.html'), name='aj02'),
    path('aj03', TemplateView.as_view(template_name='aj03.html'), name='aj03'),
    path('aj04', TemplateView.as_view(template_name='aj04.html'), name='aj04'),
    path('aj05', TemplateView.as_view(template_name='aj05.html'), name='aj05'),

    path('ajs01', views.ajs01, name='ajs01'),
    path('ajs011', views.ajs011, name='ajs011'),
    path('ajs02', views.ajs02, name='ajs02'),
    path('ajs03', views.ajs03, name='ajs03'),
    path('ajs04', views.ajs04, name='ajs04'),
]
