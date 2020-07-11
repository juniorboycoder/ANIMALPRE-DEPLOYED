"""animalpredict URL Configuration

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
from django.conf.urls import  url
from django.urls import  include


from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy, reverse

app_name= "animalpre"

urlpatterns = [
    path('admin/', admin.site.urls),

    
    #url(r'^animalpre/', animalpre.views.HomeView, name="home"),

    url(r'^animalpre/', include( 'animalpre.urls', namespace="animalpre")),
    url(r'^api/', include( 'animalpre.urls', namespace="animalpre")),

    path('accounts/', include('allauth.urls')),

      
   
]