from django.db.models import fields
from rest_framework import serializers
from .models import Client, SubTask, Task, Project

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id' ,'name', 'email', 'phoneNumber', 'address']


class SubTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id' ,'title', 'priority', 'deadline', 'daysLeft', 'status', 'responsible_client']



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id' ,'title', 'priority', 'deadline', 'daysLeft', 'status', 'responsible_client', 'subTasks']
        


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id' ,'title', 'priority', 'deadline', 'daysLeft', 'status', 'responsible_client', 'tasks']