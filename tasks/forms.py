from .models import Task
from django.forms import ModelForm
from django import forms
from .models import TaskCategory
from users.models import User


class TaskUpdateForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    deadline_dateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'
    }), required=False)
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all(), empty_label=None)

    class Meta:
        model = Task
        fields = ('description', 'deadline_dateTime', 'category', 'image')


class TaskCreateForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Заголовок задачи'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Описание задачи'
    }))
    deadline_dateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'
    }), required=False)
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all(), widget=forms.Select, empty_label=None)
    owner = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput, required=False)

    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline_dateTime', 'image', 'category', 'owner')
