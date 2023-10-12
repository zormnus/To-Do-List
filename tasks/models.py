from django.db import models
from users.models import User
from django.utils import timezone


class TaskCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Категория {self.name}'


class Task(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    creation_dateTime = models.DateTimeField(default=timezone.localtime(timezone.now()))
    finished_dateTime = models.DateTimeField(null=True, blank=True)
    deadline_dateTime = models.DateTimeField()
    image = models.ImageField(upload_to='tasks_images', null=True,
                              blank=True)
    category = models.ForeignKey(to=TaskCategory, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Задача {self.title} категории {self.category.name} от {self.creation_dateTime}'
