from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('companies/', views.getCompanies),
    path('companies/<str:pk>/', views.getCompany),
    path('companies/<str:pk>/employee/', views.addEmployee),
]
