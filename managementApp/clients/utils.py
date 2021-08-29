from datetime import datetime

from clients.models import Client, SubTask, Task, Project

#REDO

def limitPriority(calculatedPriority):
    if calculatedPriority <= 40:
        return 1;
    elif calculatedPriority > 40 and calculatedPriority <=60: 
        return 2;
    else:
        return 3;


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
        obj.deadline = compareDeadlinesForTask(obj)
        obj.save()
    
    print("Task deadline has been updated!" )


def compareDeadlinesForTask(obj):
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
        obj.deadline = compareDeadlinesForProject(obj)
        obj.save()
    
    print("Project deadline has been updated!" )


def compareDeadlinesForProject(obj):
    temp_project = obj
    save_date = datetime.date( datetime.now() )
    for task in temp_project.tasks.all():
        if  save_date < task.deadline:
            save_date = task.deadline

    return save_date   
