from django.contrib import admin
from .models import Client, SubTask, Task, Project

# Register your models here.
admin.site.register(Client)
admin.site.register(SubTask)
admin.site.register(Task)
admin.site.register(Project)