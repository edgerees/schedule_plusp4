from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    employees = Employee.objects.all()

    total_employees = employees.count()

    total_tasks = tasks.count()

    complete = tasks.filter(status='Complete').count()
    pending = tasks.filter(status='Pending').count()

    context = {'tasks': tasks, 'employees': employees,
               'total_employees': total_employees, 'total_tasks': total_tasks, 'complete': complete, 'pending': pending}

    return render(request, 'schedule_app/dashboard.html', context)


def positions(request):
    positions = Position.objects.all()
    return render(request, 'schedule_app/positions.html', {'positions': positions})


def employee(request, pk):
    employee = Employee.objects.get(id=pk)

    # tasks = employee.task_set.all()

    context = {'employee': employee}
    return render(request, 'schedule_app/employee.html', context)
