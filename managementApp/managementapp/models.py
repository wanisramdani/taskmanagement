from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query import QuerySet


class Client(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=300)
   
    def __str__(self):
        return "%s" % (self.name)

class SubTask(models.Model):
    title = models.CharField(max_length=300)
    priority = models.IntegerField()
    deadline = models.DateField(blank=True)
    daysLeft = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Unset')
    responsible_client = models.ForeignKey(
        'Client',
        on_delete=CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return " %s " % (self.title); 


class Task(models.Model):
    title = models.CharField(max_length=300)
    priority = models.IntegerField(null=True ,blank=True)
    deadline = models.DateField(null=True, blank=True)
    daysLeft = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Unset')
    responsible_client = models.ForeignKey(
        Client,
        on_delete=CASCADE,
        blank=True, null=True
    )
    
    subTasks = models.ManyToManyField(
        SubTask,
        blank=True,
    )
    def __str__(self):
        return " %s " % (self.title); 


class Project(models.Model):
    title = models.CharField(max_length=300)
    priority = models.IntegerField(null=True ,blank=True)
    deadline = models.DateField(null=True, blank=True)
    daysLeft = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Unset')
    responsible_client = models.ForeignKey(
        Client, default="UNASSIGNED",
        on_delete=CASCADE,
        blank=True, null=True
    )
    tasks = models.ManyToManyField(
        Task, default="UNASSIGNED",
        blank=True, 
    )
   
    def __str__(self):
        return " %s " % (self.title); 




