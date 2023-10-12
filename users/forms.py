from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите ваше имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите вашу фамилию'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите вашу почту'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль ещё раз'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'image', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': True}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input d-none', 'id': 'imageInput'}),
                             required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'email', 'username')
