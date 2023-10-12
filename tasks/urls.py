from django.urls import path
from .views import TasksListView, TaskUpdateView, task_status_update, \
    user_recent_activity, TasksProgressView, TasksCreateView, user_favourite_categories


app_name = 'tasks'

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='tasks'),
    path('page/<int:page>', TasksListView.as_view(), name='paginator'),
    path('task_create/', TasksCreateView.as_view(), name='task_create'),
    path('recent_stats', user_recent_activity, name='recent_stats'),
    path('fav_cats', user_favourite_categories, name='fav_cats'),
    path('task_update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task_status_update/<int:task_id>/', task_status_update, name='task_status_update'),
    path('tasks_progress/', TasksProgressView.as_view(), name='task_progress'),
]
