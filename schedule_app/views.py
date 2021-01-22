from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *

from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'schedule_app/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

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
