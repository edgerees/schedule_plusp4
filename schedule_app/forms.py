from django.forms import ModelForm
from .models import Task, Position
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
