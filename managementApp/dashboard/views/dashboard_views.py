from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from managementapp.models import Client, Project, Task, SubTask
from .filterData import clientsObjectsData, clientsAllData


def index(request):
    return render(request, "dashboard/dashboard.html", {})

def clientDash(request):
    return render(request, "dashboard/clientDash.html", {})

def ClientData(request):
    dataset = Client.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def subtaskData(request):
    dataset = SubTask.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def taskData(request):
    dataset = Task.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def projectData(request):
    dataset = Project.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def allClientData(request):
    dataset = clientsAllData()
    return JsonResponse(dataset, safe=False)


## Client total projects filtered by status and Priority
# low&mid&high  projects
def clientsLowProjectData(request):
    dataset = clientsObjectsData(Project ,1)
    return JsonResponse(dataset, safe=False)


def clientsMidProjectData(request):
    dataset = clientsObjectsData(Project, 2)
    return JsonResponse(dataset, safe=False)


def clientsHighProjectData(request):
    dataset = clientsObjectsData(Project ,3)
    return JsonResponse(dataset, safe=False)


## Client total tasks filtered by status and Priority
# low&mid&high  tasks
def clientsLowTaskData(request):
    dataset = clientsObjectsData(Task ,1)
    return JsonResponse(dataset, safe=False)


def clientsMidTaskData(request):
    dataset = clientsObjectsData(Task, 2)
    return JsonResponse(dataset, safe=False)


def clientsHighTaskData(request):
    dataset = clientsObjectsData(Task ,3)
    return JsonResponse(dataset, safe=False)


## Client total subtasks filtered by status and Priority
# low&mid&high  subtasks
def clientsLowSubtaskData(request):
    dataset = clientsObjectsData(SubTask ,1)
    return JsonResponse(dataset, safe=False)


def clientsMidSubtaskData(request):
    dataset = clientsObjectsData(SubTask, 2)
    return JsonResponse(dataset, safe=False)


def clientsHighSubtaskData(request):
    dataset = clientsObjectsData(SubTask ,3)
    return JsonResponse(dataset, safe=False)