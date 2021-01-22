from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('landing/', views.landing, name='landing'),
    path('positions/', views.positions, name='positions'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('create_task/<str:pk>/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
    path('task_details/<str:pk>/', views.taskDetails, name='task_details'),
    path('create_position/', views.createPosition, name='create_position'),
    path('delete_position/<str:pk>/',
         views.deletePosition, name='delete_position'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
