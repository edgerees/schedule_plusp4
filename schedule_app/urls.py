from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('user/', views.userPage, name='user-page'),
    path('positions/', views.positions, name='positions'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('create_task/<str:pk>/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('update_status/<str:pk>/', views.updateStatus, name='update_status'),
    path('update_employee/<str:pk>/',
         views.updateEmployee, name='update_employee'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
    path('task_details/<str:pk>/', views.taskDetails, name='task_details'),
    path('create_position/', views.createPosition, name='create_position'),
    path('delete_position/<str:pk>/',
         views.deletePosition, name='delete_position'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('chat/', views.chat, name="chat"),
    path('chat/<str:room_name>/', views.room, name="room"),
    path('account/', views.accountSettings, name="account"),
]
