from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets, permissions

from .models import Client, SubTask, Task, Project
from . import forms, serializers

from datetime import datetime

def list(request):
    setFields()
    return render(request, 'clients/list.html', 
                            {'clientsList': Client.objects.all(),
                                'subTasks': SubTask.objects.all(),
                                'Tasks': Task.objects.all(),
                                'Projects': Project.objects.all(),
                            }
                )

def setFields():
    setTaskPriority()
    setTaskDeadline()
    setProjectPriority()
    setProjectDeadline()

def clientList(request):
    if request.method == 'POST':
        addClientForm = forms.addClient(request.POST)
        if addClientForm.is_valid():
            addClientForm.save()
            return redirect("clients:clientList")
    else:
        addClientForm = forms.addClient()
        
    return render(request, 'clients/list/clientList.html', {
        'clientsList': Client.objects.all(),
        'addClientForm': addClientForm
        } 
        )

def subTaskList(request):
    return render(request, 'clients/list/subTaskList.html', {'subTasks': SubTask.objects.all()} )

def taskList(request):
    setTaskPriority()
    setTaskDeadline()
    return render(request, 'clients/list/taskList.html', {'Tasks': Task.objects.all(),})

def projectList(request):
    setProjectPriority()
    setProjectDeadline()
    return render(request, 'clients/list/projectList.html', {'Projects': Project.objects.all()})
###################

def limitPriority(calculatedPriority):
    if calculatedPriority <= 40:
        return 1;
    elif calculatedPriority > 40 and calculatedPriority <=60: 
        return 2;
    else:
        return 3;

# CLIENT CRUD

def clientProfile(request, id):
    client = get_object_or_404(Client, id=id)    
    client_projects = Project.objects.filter(responsible_client=client)
    return render(request, 'clients/profile/client.html', {'client': client, 'projects': client_projects} )

def subtaskProfile(request, id):
    subtask = get_object_or_404(SubTask, id=id)
    subtask_tasks = Task.objects.filter(subTasks=subtask)
    return render(request, 'clients/profile/subtask.html', {'subtask': subtask, 'tasks': subtask_tasks})

def taskProfile(request, id):
    task = get_object_or_404(Task, id=id)
    task_project = Project.objects.filter(tasks=task)
    return render(request, 'clients/profile/task.html', {'task': task, 'projects': task_project})

def projectProfile(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'clients/profile/project.html', {'project': project})



def addClient(request):
    if request.method == 'POST':
        addClientForm = forms.addClient(request.POST)
        if addClientForm.is_valid():
            addClientForm.save()
            return redirect("clients:clientList")
    else:
        addClientForm = forms.addClient()

    return render(request, 'clients/add/addClient.html', {'addClientForm': addClientForm})

def updateClient(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        updateClientForm = forms.addClient(request.POST or None, instance=client)
        if updateClientForm.is_valid():
            updateClientForm.save()
            return redirect("clients:clientList")
    else:
        data = {
            "name": client.name,
            "email": client.email,
            "phoneNumber": client.phoneNumber,
            "address": client.address,
        }
        addClientForm = forms.addClient(initial=data)
    return render(request, 'clients/add/addClient.html', {'addClientForm': addClientForm})
        
        
def deleteClient(request, id):
    Client.objects.filter(pk=id).delete()
    return redirect("clients:clientList")

# SUBTASK CRUD

def addSubTask(request):
    if request.method == 'POST':
        addSubTaskForm = forms.addSubTask(request.POST)
        if addSubTaskForm.is_valid():
            addSubTaskForm.save()
            # "subTasks:list"
            return redirect("clients:subTaskList")
    else:
        addSubTaskForm = forms.addSubTask()
    
    return render(request, 'clients/add/addSubTask.html', {'addSubTaskForm': addSubTaskForm})

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

    return render(request, 'clients/add/addSubTask.html', {'addSubTaskForm': addSubTaskForm})

def deleteSubTask(request, id):
    Client.objects.filter(pk=id).delete()
    return redirect("clients:subTaskList") 

# TASK CRUD

def addTask(request):
    if request.method == 'POST':
        addTaskForm = forms.addTask(request.POST)
        if addTaskForm.is_valid():
            addTaskForm.save()
            return redirect("clients:taskList")
    else:
        addTaskForm = forms.addTask()

    return render(request, 'clients/add/addTask.html', {'addTaskForm': addTaskForm})

# PROJECT CRUD

def addProject(request):
    if request.method == 'POST':
        addProjectForm = forms.addProject(request.POST)
        if addProjectForm.is_valid():
            addProjectForm.save()
            return redirect("clients:projectList")
    else:
        addProjectForm = forms.addProject()

    return render(request, 'clients/add/addProject.html', {'addProjectForm': addProjectForm})


### API endpoint

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.AllowAny]

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = serializers.SubTaskSerializer
    permission_classes = [permissions.AllowAny]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.AllowAny]

##### TASK

def setTaskPriority():
    obj = Task.objects.all()
    for obj in Task.objects.all():
        obj.priority = limitPriority( calculateTaskPriority(obj) )
        obj.save()
    print("Task priority has been updated!" )

# Moy
def calculateTaskPriority(obj):
    sumPriority = 0
    for sub in obj.subTasks.all():
        sumPriority += sub.priority
    
    return sumPriority / 5

def setTaskDeadline():
    obj = Task.objects.all()
    for obj in Task.objects.all():
        obj.deadline = compareDealinesForTask(obj)
        obj.save()
    
    print("Task deadline has been updated!" )


def compareDealinesForTask(obj):
    temp_task = obj
    save_date = datetime.date( datetime.now() )
    for sub in temp_task.subTasks.all():
        if  save_date < sub.deadline:
            save_date = sub.deadline

    return save_date            
            
##### PROJECT

def setProjectPriority():
    obj = Project.objects.all()
    for obj in Project.objects.all():
        obj.priority = limitPriority( calculateProjectPriority(obj) )
        obj.save()
    print("Project priority has been updated!" )

# Moy
def calculateProjectPriority(obj):
    sumPriority = 0
    for task in obj.tasks.all():
        sumPriority += task.priority

    return sumPriority / 5


def setProjectDeadline():
    obj = Project.objects.all()
    for obj in Project.objects.all():
        obj.deadline = compareDealinesForProject(obj)
        obj.save()
    
    print("Project deadline has been updated!" )


def compareDealinesForProject(obj):
    temp_project = obj
    save_date = datetime.date( datetime.now() )
    for task in temp_project.tasks.all():
        if  save_date < task.deadline:
            save_date = task.deadline

    return save_date   



