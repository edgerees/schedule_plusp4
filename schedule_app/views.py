from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import ChatForm, TaskForm, PositionForm
from .filters import TaskFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Views here
from .forms import TaskForm, PositionForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def landing(request):
    return render(request, 'schedule_app/landing.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='employee')
            user.groups.add(group)
            # Added username after video because of error returning employee name if not added
            Employee.objects.create(
                user=user,
                name=user.username,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'schedule_app/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'schedule_app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    tasks = Task.objects.all()
    employees = Employee.objects.all()

    total_employees = employees.count()

    total_tasks = tasks.count()
    in_progress = tasks.filter(status='In Progress').count()
    pending = tasks.filter(status='Pending').count()

    tasks.filter(status='Complete').delete()

    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs

    context = {'tasks': tasks, 'employees': employees,
               'total_employees': total_employees,
               'total_tasks': total_tasks,
               'in_progress': in_progress,
               'pending': pending, 'myFilter': myFilter}

    return render(request, 'schedule_app/dashboard.html', context)


@login_required(login_url='login')
def userPage(request):
    return render(request, 'schedule_app/user.html')


@login_required(login_url='login')
def positions(request):
    positions = Position.objects.all()
    return render(request, 'schedule_app/positions.html', {'positions': positions})


def about(request):
    return render(request, 'schedule_app/about.html')


@login_required(login_url='login')
def employee(request, pk):
    employee = Employee.objects.get(id=pk)

    tasks = employee.task_set.all()

    total_tasks = tasks.count()

    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs

    context = {'employee': employee,
               'tasks': tasks, 'total_tasks': total_tasks, 'myFilter': myFilter}
    return render(request, 'schedule_app/employee.html', context)


@login_required(login_url='login')
def createTask(request, pk):
    TaskFormSet = inlineformset_factory(
        Employee, Task, fields=('title', 'note', 'status', 'priority', 'date_due'), extra=5)
    employee = Employee.objects.get(id=pk)
    formset = TaskFormSet(queryset=Task.objects.none(), instance=employee)
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, instance=employee)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'schedule_app/task_form.html', context)


@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    formset = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'schedule_app/task_form.html', context)


@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'title': task}

    return render(request, 'schedule_app/delete.html', context)


def taskDetails(request, pk):
    task = Task.objects.get(id=pk)

    context = {'task': task}

    return render(request, 'schedule_app/task_details.html', context)


def createPosition(request):

    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/positions')

    context = {'form': form}

    return render(request, 'schedule_app/position_form.html', context)


def deletePosition(request, pk):
    position = Position.objects.get(id=pk)

    if request.method == 'POST':
        position.delete()
        return redirect('/positions')

    context = {'title': position}

    return render(request, 'schedule_app/delete_position.html', context)


def room(request, room_name):
    return render(request, 'schedule_app/chatroom.html', {
        'room_name': room_name
    })


def chat(request):
    form = ChatForm()

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            chat_id = form.cleaned_data.get("chatroom")
            return redirect('/chat/' + chat_id)

    context = {'form': form}

    return render(request, 'schedule_app/chat_selection.html', context)
