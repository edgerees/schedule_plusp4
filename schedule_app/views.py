from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'schedule_app/dashboard.html')

def tasks(request):
    return render(request,'schedule_app/tasks.html')

def employee(request):
    return render(request,'schedule_app/employee.html')

