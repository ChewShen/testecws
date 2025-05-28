from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registerPage/', views.registerPage, name="registerPage"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
