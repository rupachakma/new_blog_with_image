from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addpost', views.addpost, name="addpost"),
    path('updatepage<int:id>', views.updatepage, name="updatepage"),
    path('signuppage', views.signuppage, name="signuppage"),
    path('loginpage', views.loginpage, name="loginpage"),
]
