from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query import QuerySet
from django.template.defaultfilters import title


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
    responsible_client = models.ForeignKey(
        Client,
        on_delete=CASCADE,
        blank=True, null=True
    )
    tasks = models.ManyToManyField(
        Task,
        blank=True, 
    )
    def __str__(self):
        return " %s " % (self.title); 




