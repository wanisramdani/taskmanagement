from datetime import datetime

from clients.models import Client, SubTask, Task, Project

#REDO

def limitPriority(calculatedPriority):
    if calculatedPriority <= 1:
        return 1;
    elif calculatedPriority > 1 and calculatedPriority <=2: 
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
    # 5 should be replaced by a function that gives the sum of all priorities
    return sumPriority / 5 

def setTaskDeadline():
    obj = Task.objects.all()
    for obj in Task.objects.all():
        obj.deadline, obj.daysLeft = compareDeadlinesForTask(obj)
        obj.save()
    
    print("Task deadline has been updated!" )


def compareDeadlinesForTask(obj):
    temp_task = obj
    saved_deadline = datetime.date( datetime.now() )
    days_left = 0
    for sub in temp_task.subTasks.all():
        if  saved_deadline < sub.deadline:
            saved_deadline = sub.deadline

    days_left = countDaysLeft(saved_deadline)
    return saved_deadline, days_left           
            
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
        obj.deadline, obj.daysLeft = compareDeadlinesForProject(obj)
        obj.save()
    
    print("Project deadline has been updated!" )
    

def compareDeadlinesForProject(obj):
    temp_project = obj
    saved_deadline = datetime.date( datetime.now() )
    days_left = 0
    for task in temp_project.tasks.all():
        if  saved_deadline < task.deadline:
            saved_deadline = task.deadline

    days_left = countDaysLeft(saved_deadline)
    return saved_deadline, days_left

# replace SubTask by obj and use it with the rest of the models
def saveDaysLeft(instances):
    for obj in instances.objects.all():
        obj.daysLeft = countDaysLeft(obj.deadline)
        obj.save()

def countDaysLeft(deadline):
    return ( deadline - datetime.date( datetime.now() ) ).days
