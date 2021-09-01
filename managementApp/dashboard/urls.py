from django.urls import path
from . import views

app_name= 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientDash/', views.clientDash, name='clientDash'),

    path('clientsData/', views.ClientData, name='data'),
    path('subtaskData/', views.subtaskData, name='data'),
    path('tasksData/', views.taskData, name='data'),
    path('projectData/', views.projectData, name='data'),
    
    # low&mid&high  projects
    path('clientsProjectLowData/', views.clientsLowProjectData, name='data' ),
    path('clientsProjectMidData/', views.clientsMidProjectData, name='data' ),
    path('clientsProjectHighData/', views.clientsHighProjectData, name='data' ),

    # low&mid&high  tasks
    path('clientsTaskLowData/', views.clientsLowTaskData, name='data' ),
    path('clientsTaskMidData/', views.clientsMidTaskData, name='data' ),
    path('clientsTaskHighData/', views.clientsHighTaskData, name='data' ),

    # low&mid&high  subtask
    path('clientsSubtaskLowData/', views.clientsLowSubtaskData, name='data' ),
    path('clientsSubtaskMidData/', views.clientsMidSubtaskData, name='data' ),
    path('clientsSubtaskHighData/', views.clientsHighSubtaskData, name='data' ),

]