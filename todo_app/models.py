from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """
    Extending the Base User Model
    """
    class Meta:
        db_table = 'user'


class Todo(models.Model):
    """
    Todo model
    """

    no = models.AutoField(primary_key=True)
    task = models.CharField('task', max_length=100)
    is_done = models.BooleanField('is_done', default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f"{str(self.no)}:{self.is_done}"  

    class Meta:
        db_table = 'todo'
        ordering = ['created_at']
        verbose_name = 'todo'
        verbose_name_plural = 'todo'
