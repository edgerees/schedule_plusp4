from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import TaskForm
from .filters import TaskFilter

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

    tasks = employee.task_set.all()

    total_tasks = tasks.count()

    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs

    context = {'employee': employee,
               'tasks': tasks, 'total_tasks': total_tasks, 'myFilter': myFilter}
    return render(request, 'schedule_app/employee.html', context)


def createTask(request, pk):
    TaskFormSet = inlineformset_factory(
        Employee, Task, fields=('title', 'description', 'status', 'priority', 'date_due'), extra=5)
    employee = Employee.objects.get(id=pk)
    formset = TaskFormSet(queryset=Task.objects.none(), instance=employee)
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, instance=employee)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'schedule_app/task_form.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'schedule_app/task_form.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'title': task}

    return render(request, 'schedule_app/delete.html', context)
