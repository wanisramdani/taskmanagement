from django.shortcuts import get_object_or_404, redirect, render

from managementapp import forms
from managementapp.models import Client, Project, SubTask, Task
from managementapp.utils import saveDaysLeft


def subTaskList(request):
    saveDaysLeft(SubTask)
    return render(request, 'clients/list/subTaskList.html', {
        'subTasks': SubTask.objects.all()
        } )


def subtaskProfile(request, id):
    subtask = get_object_or_404(SubTask, id=id)
    subtask_tasks = Task.objects.filter(subTasks=subtask)
    return render(request, 'clients/profile/subtask.html', {
        'subtask': subtask, 
        'tasks': subtask_tasks
        })


def addSubTask(request):
    if request.method == 'POST':
        addSubTaskForm = forms.addSubTask(request.POST)
        if addSubTaskForm.is_valid():
            addSubTaskForm.save()
            # "subTasks:list"
            return redirect("clients:subTaskList")
    else:
        addSubTaskForm = forms.addSubTask()
    
    return render(request, 'clients/add/addSubTask.html', {
        'addSubTaskForm': addSubTaskForm
        })


def updateSubtask(request, id):
    subtask = get_object_or_404(SubTask, id=id)
    if request.method == 'POST':
        addSubTaskForm = forms.addSubTask(request.POST or None, instance=subtask)
        if addSubTaskForm.is_valid():
            addSubTaskForm.save()
            return redirect("clients:subTaskList") 
    else:
        data = {
            "title": subtask.title,
            "priority": subtask.priority,
            "deadline": subtask.deadline,
            "responsible_client": subtask.responsible_client,
        }
        addSubTaskForm = forms.addSubTask(initial=data)

    return render(request, 'clients/add/addSubTask.html', {
        'addSubTaskForm': addSubTaskForm
        })


def deleteSubTask(request, id):
    Client.objects.filter(pk=id).delete()
    return redirect("clients:subTaskList") 
