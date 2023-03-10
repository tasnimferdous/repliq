from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('company-info/<str:pk>/', views.companyInfo, name = "info"),
    path('sign-up/', views.signUp, name = "signup"),
    path('sign-in/', views.signIn, name = "signin"),
]
