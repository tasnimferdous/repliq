from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('sign-up/', views.signUp, name = "signup"),
    path('sign-in/', views.signIn, name = "signin"),
]
