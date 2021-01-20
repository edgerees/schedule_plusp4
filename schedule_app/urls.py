from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tasks/', views.tasks),
    path('employee/', views.employee),
]
