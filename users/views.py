from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, reverse
from django.utils import timezone
from django.views.generic import TemplateView, FormView, View, DetailView, UpdateView

from tasks.models import Task
from .forms import UserLoginForm, UserRegForm, UserProfileForm
from .models import User
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'home.html'
    title = 'To Do - Главная'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth_form'] = UserLoginForm()
        context['reg_form'] = UserRegForm()
        return context


class AboutView(TitleMixin, TemplateView):
    template_name = 'about.html'
    title = 'To Do - О нас'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileView(TemplateView):
    template_name = 'account_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.request.user.username} - Профиль'
        context['form'] = UserProfileForm(instance=self.request.user)
        return context


class UserAuthView(FormView):
    form_class = UserLoginForm
    success_url = '/home/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserAuthView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('home'))


class UserRegView(FormView):
    form_class = UserRegForm
    success_url = '/home/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(UserRegView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse('users:profile')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))
