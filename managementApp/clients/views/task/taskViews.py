from django.shortcuts import get_object_or_404, redirect, render

from clients import forms
from clients.models import Client, Project, SubTask, Task

from clients.utils import limitPriority, setTaskPriority, setTaskDeadline


def taskList(request):
    setTaskPriority()
    setTaskDeadline()
    return render(request, 'clients/list/taskList.html', {'Tasks': Task.objects.all(),})


def taskProfile(request, id):
    task = get_object_or_404(Task, id=id)
    task_project = Project.objects.filter(tasks=task)
    return render(request, 'clients/profile/task.html', {'task': task, 'projects': task_project})


# CRUD
def addTask(request):
    if request.method == 'POST':
        addTaskForm = forms.addTask(request.POST)
        if addTaskForm.is_valid():
            addTaskForm.save()
            return redirect("clients:taskList")
    else:
        addTaskForm = forms.addTask()

    return render(request, 'clients/add/addTask.html', {'addTaskForm': addTaskForm})
