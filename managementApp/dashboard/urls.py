from django.urls import path
from . import views

app_name= 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientsData/', views.ClientData, name='data'),
    path('subtaskData/', views.subtaskData, name='data'),
    path('tasksData/', views.taskData, name='data'),
    path('projectData/', views.projectData, name='data'),
    
    # low&mid&high Delayed projects
    path('clientsLowData/', views.clientsLowProjectData, name='data' ),
    path('clientsMidData/', views.clientsMidProjectData, name='data' ),
    path('clientsHighData/', views.clientsHighProjectData, name='data' ),

]