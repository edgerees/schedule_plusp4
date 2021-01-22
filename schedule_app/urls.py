from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
   
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
    path('about/', views.about, name='about'),
<<<<<<< HEAD
    
    path('user/', views.userPage, name='user-page'),
=======
    path('landing/', views.landing, name='landing'),
>>>>>>> 6cbfb55e419d41abec292dc59fd03996553ea9db
    path('positions/', views.positions, name='positions'),
    path('employee/<str:pk>/', views.employee, name='employee'),

    path('create_task/<str:pk>/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
<<<<<<< HEAD

=======
    path('task_details/<str:pk>/', views.taskDetails, name='task_details'),
    path('create_position/', views.createPosition, name='create_position'),
    path('delete_position/<str:pk>/',
         views.deletePosition, name='delete_position'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
>>>>>>> 6cbfb55e419d41abec292dc59fd03996553ea9db
]
