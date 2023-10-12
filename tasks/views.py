from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from common.views import TitleMixin

from .forms import TaskCreateForm, TaskUpdateForm
from .models import Task
from .tasks_services import (get_in_process_tasks, get_last_finished_tasks,
                             get_most_favourite_categories,
                             get_recent_tasks_stats, get_task)


class TasksListView(TitleMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    paginate_by = 4
    title = 'To Do - Задачи'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksListView, self).get_context_data()
        context['tasks_edit_forms'] = [TaskUpdateForm(
            instance=task) for task in self.get_queryset()]
        context['create_task_form'] = TaskCreateForm()
        return context

    def get_queryset(self):
        return get_in_process_tasks(owner=self.request.user)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm

    def get_success_url(self):
        return reverse('tasks:tasks')


@login_required
def task_status_update(request, task_id):
    """Сервис, устанавливающий статус таска в законченный"""
    if request.method == 'POST':
        task = get_task(task_id)
        task.is_finished = True
        task.finished_dateTime = timezone.localtime(timezone.now())
        task.save()
        return HttpResponseRedirect(reverse('tasks:tasks'))
    elif request.method == 'GET':
        return HttpResponseRedirect(reverse('tasks:tasks'))


class TasksProgressView(TemplateView):
    template_name = 'progress.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.request.user.username} - Статистика'
        context['recent_tasks'] = get_last_finished_tasks(
            owner=self.request.user)
        return context


class TasksCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks:tasks')


@login_required
def user_recent_activity(request):
    """Сервис, возвращающий данные о недавней активности пользователя
     (последние 6 месяцев)
    """
    return JsonResponse(get_recent_tasks_stats(request.user), safe=False)


@login_required
def user_favourite_categories(request):
    """Сервис, возвращающий данные о самых востребованных категориях пользователя"""
    return JsonResponse(get_most_favourite_categories(request.user), safe=False)
