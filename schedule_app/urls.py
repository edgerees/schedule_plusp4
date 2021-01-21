from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('positions/', views.positions),
    path('employee/<str:pk>/', views.employee),
]
