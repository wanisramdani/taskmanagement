from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from managementapp.models import Client, Project, Task, SubTask
from .filterData import clientsObjectsData


def index(request):
    return render(request, "dashboard/dashboard.html", {})


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


## Client total projects filtered by status and Priority
# low&mid&high  projects
def clientsLowProjectData(request):
    dataset = clientsObjectsData(Project ,1)
    print(dataset)
    return JsonResponse(dataset, safe=False)


def clientsMidProjectData(request):
    dataset = clientsObjectsData(Project, 2)
    print(dataset)
    return JsonResponse(dataset, safe=False)


def clientsHighProjectData(request):
    dataset = clientsObjectsData(Project ,3)
    return JsonResponse(dataset, safe=False)