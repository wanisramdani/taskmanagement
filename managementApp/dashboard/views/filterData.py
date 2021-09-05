from django.http.response import HttpResponse

from managementapp.models import Client, Project, Task, SubTask
from .dashboard_views import *

def ezData(dataset):
    for data in dataset:
        for obj in data:
            res ={
                "name": data.name,
                "email": data.email,
                "title": obj.title,
            }
    print(res)
    return res

def clientsAllData():
    dataset = []
    for client in Client.objects.all():
        client_project = Project.objects.filter(responsible_client=client)
        client_task = Task.objects.filter(responsible_client=client)
        client_subtask = SubTask.objects.filter(responsible_client=client)
        data = {
            "name": client.name,
            "email": client.email,
            "subtask":  getObjectData(client_subtask),
            "task": getObjectData(client_task),
            "project": getObjectData(client_project),
        }
        dataset.append(data)

    return dataset

def getObjectData(objects):
    dict = {}
    for obj in objects:
        return {
            "title": obj.title,
            "priority": obj.priority,
            "deadline": obj.deadline,
            "daysLeft": obj.daysLeft,
        }
        dict.append(res)
        
    
    return dict


# How many projects each client has, filtered by priority&status
# Return {project_priority, client_name, project_status}
def clientsObjectsData(object, priority):
    dataset = []
    for client in Client.objects.all():
        client_objects = object.objects.filter(responsible_client=client)
        
        data = {
            'name': client.name, 
            'priority': getPriority(client_objects),
            'total_delayed': countTotalProjects(client, client_objects, priority, "Delayed"),
            'total_wip': countTotalProjects(client, client_objects, priority, "Work in progress"),
            'total_completed': countTotalProjects(client, client_objects, priority, "Completed"),
        }
        dataset.append(data)

    return dataset


def countTotalProjects(client, objects, priority, status):
    total = 0
    for obj in objects:
        if obj.status == status and obj.responsible_client == client:
            total += 1

    return total

def getPriority(objects):
    if not objects:
        return "UNSET"

    for obj in objects:
        if obj.priority == 1:
            return "LOW"
        elif obj.priority == 2:
            return "MID"
        else: 
            return "HIGH"