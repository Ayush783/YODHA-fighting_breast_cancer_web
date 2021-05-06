from django.contrib import admin
from django.urls import path,include

from api import views

urlpatterns = [
    path('/', views.apihome, name = 'apihome'),
    path('/signup', views.signup, name = 'signup'),
]
