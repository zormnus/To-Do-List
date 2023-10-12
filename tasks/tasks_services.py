from datetime import datetime

from django.db.models import Count
from django.utils import timezone

from .models import Task, TaskCategory


def get_in_process_tasks(owner):
    queryset = Task.objects.filter(is_finished=False,
                                   deadline_dateTime__gte=timezone.now(), owner=owner).select_related('category')
    return queryset


def get_recent_tasks_stats(owner):
    six_months_ago = timezone.now() - timezone.timedelta(days=180)
    completed_tasks = Task.objects.filter(
        owner=owner,
        is_finished=True,
        finished_dateTime__gte=six_months_ago,
        finished_dateTime__lte=timezone.now()
    ).select_related('category')
    return parse_tasks_by_months(completed_tasks)


def get_most_favourite_categories(owner):
    data = Task.objects.values('category__name').filter(owner=owner). \
        annotate(frequency=Count('category_id')).order_by('-frequency')[:10]
    result = {row['category__name']: row['frequency'] for row in data}
    return result


def parse_tasks_by_months(completed_tasks):
    months = [
        'Январь', 'Февраль', 'Март', 'Апрель',
        'Май', 'Июнь', 'Июль', 'Август',
        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    ]
    data = {}

    current_month = datetime.now().month

    for _ in range(6):
        current_month -= 1
        if current_month == 0:
            current_month = 12
        data[months[current_month]] = 0

    for task in completed_tasks:
        task_month = months[task.finished_dateTime.month - 1]
        if task_month in data:
            data[task_month] += 1
        else:
            data[task_month] = 1

    return data


def get_last_finished_tasks(owner):
    return Task.objects.filter(owner=owner, is_finished=True).order_by('-finished_dateTime')\
               .values('title', 'description', 'finished_dateTime')[:10]


def get_task(task_id):
    return Task.objects.get(pk=task_id)
