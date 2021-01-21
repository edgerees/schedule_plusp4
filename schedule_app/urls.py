from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('positions/', views.positions),
    path('employee/<str:pk>/', views.employee),
    path('create_task/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
]
