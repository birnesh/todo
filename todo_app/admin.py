from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from todo_app import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Todo)

