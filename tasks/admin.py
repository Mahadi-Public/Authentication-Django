from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tasks.models import TaskList

# Unregister the default UserAdmin
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'password', 'is_superuser', 'last_login',  'is_active', 'date_joined']


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ['id','title','images','price','category']
