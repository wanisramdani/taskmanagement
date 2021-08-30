from django.shortcuts import get_object_or_404, redirect, render

from managementapp import forms
from managementapp.models import Project

from managementapp.utils import setProjectPriority, setProjectDeadline


def projectList(request):
    setProjectPriority()
    setProjectDeadline()
    return render(request, 'clients/list/projectList.html', {
        'Projects': Project.objects.all(), 
        })


def projectProfile(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'clients/profile/project.html', {
        'project': project
        })


# CRUD
def addProject(request):
    if request.method == 'POST':
        addProjectForm = forms.addProject(request.POST)
        if addProjectForm.is_valid():
            addProjectForm.save()
            return redirect("clients:projectList")
    else:
        addProjectForm = forms.addProject()

    return render(request, 'clients/add/addProject.html', {
        'addProjectForm': addProjectForm
        })

