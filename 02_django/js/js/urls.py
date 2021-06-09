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

]
