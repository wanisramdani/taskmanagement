from django.shortcuts import get_object_or_404, redirect, render

from clients import forms
from clients.models import Client, Project, SubTask, Task

from clients.utils import limitPriority


def clientList(request):
    if request.method == 'POST':
        addClientForm = forms.addClient(request.POST)
        if addClientForm.is_valid():
            addClientForm.save()
            return redirect("clients:clientList")
    else:
        addClientForm = forms.addClient()
        
    return render(request, 'clients/list/clientList.html', {
        'clientsList': Client.objects.all(),
        'addClientForm': addClientForm})


def clientProfile(request, id):
    client = get_object_or_404(Client, id=id)    
    client_projects = Project.objects.filter(responsible_client=client)
    return render(request, 'clients/profile/client.html', {
        'client': client, 
        'projects': client_projects
        })

## CRUD
def addClient(request):
    if request.method == 'POST':
        addClientForm = forms.addClient(request.POST)
        if addClientForm.is_valid():
            addClientForm.save()
            return redirect("clients:clientList")
    else:
        addClientForm = forms.addClient()

    return render(request, 'clients/add/addClient.html', {
        'addClientForm': addClientForm
        })


def updateClient(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        updateClientForm = forms.addClient(request.POST or None, instance=client)
        if updateClientForm.is_valid():
            updateClientForm.save()
            return redirect("clients:clientList")
    else:
        data = {
            "name": client.name,
            "email": client.email,
            "phoneNumber": client.phoneNumber,
            "address": client.address,
        }
        addClientForm = forms.addClient(initial=data)

    return render(request, 'clients/add/addClient.html', {
        'addClientForm': addClientForm
        })
        
        
def deleteClient(request, id):
    Client.objects.filter(pk=id).delete()
    return redirect("clients:clientList")

