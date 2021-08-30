
from django.shortcuts import render

from managementapp.models import Client, SubTask, Task, Project
from managementapp.utils import setTaskPriority, setTaskDeadline, setProjectPriority, setProjectDeadline


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