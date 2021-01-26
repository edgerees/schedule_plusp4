from django.forms import ModelForm
from .models import Task, Position, Chat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'note', 'date_due', 'priority', 'employee']


class TaskStatusForm(ModelForm):
    class Meta:
        model = Task
        fields = ['status']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
