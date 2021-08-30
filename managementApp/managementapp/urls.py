from django.urls import path
from . import views

app_name= 'clients'

urlpatterns = [
    path('', views.list, name='list'),
    path('clientList/', views.clientList, name='clientList'),
    path('subTaskList/', views.subTaskList, name='subTaskList'),
    path('taskList/', views.taskList, name='taskList'),
    path('projectList/', views.projectList, name='projectList'),
        
    path('clientProfile/<int:id>', views.clientProfile, name='clientProfile'),
    path('subtaskProfile/<int:id>', views.subtaskProfile, name='subtaskProfile'),
    path('taskProfile/<int:id>', views.taskProfile, name='taskProfile'),
    path('projectProfile/<int:id>', views.projectProfile, name='projectProfile'),

    path('addClient', views.addClient, name='addClient'),
    path('addSubTask', views.addSubTask, name='addSubTask'),
    path('addTask', views.addTask, name='addTask'),
    path('addProject', views.addProject, name='addProject'),

    path('updateClient/<int:id>', views.updateClient, name='updateClient'),
    path('updateSubtask/<int:id>', views.updateSubtask, name='updateSubtask'),

    path('deleteClient/<int:id>', views.deleteClient, name='deleteClient'),
    path('deleteSubTask/<int:id>', views.deleteSubTask, name='deleteSubTask'),

]