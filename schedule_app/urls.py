from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('positions/', views.positions, name='positions'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('create_task/<str:pk>/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
]
