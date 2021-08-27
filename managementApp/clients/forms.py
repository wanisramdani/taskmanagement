from logging import PlaceHolder
from django.forms import widgets
from django.forms.fields import MultipleChoiceField
from django import forms

from crispy_forms.layout import Button, Layout, Field, Submit
from crispy_forms.helper import FormHelper

from . import models


class addClient(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    '''
    helper = FormHelper()
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('name', css_class="form-control", PlaceHolder="Name"),
        Field('email', css_class="form-control", PlaceHolder="Email"),
        Field('phoneNumber', css_class="form-control", typ="date", PlaceHolder="Phone"),
        Field('address', PlaceHolder="Address"),
        Submit('Submit', 'Submit')
    )
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(addClient, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Client
        fields = ['name', 'email', 'phoneNumber', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'phoneNumber': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholer': 'Phone',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            })

        }

class addSubTask(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = models.SubTask
        fields = ['title', 'priority', 'deadline', 'responsible_client']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'priority': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Priority - [1-3]',
                'min': '1',
                'max': '3', 
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholer': 'Deadline',
                'type':'date',
            }),

        }
        
class addTask(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False;
    helper.layout = Layout(
        Field('title', css_class="form-control", PlaceHolder="Title"),
        Field('responsible_client', PlaceHolder="Responsible Client"),
        Field('subTasks',css_class="custom-select", PlaceHolder="SubTasks"),
        Submit('Submit', 'Submit')
    )
    class Meta:
        model = models.Task
        fields = ['title', 'responsible_client', 'subTasks']
        



class addProject(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False;
    helper.layout = Layout(
        Field('title', css_class="form-control", PlaceHolder="Title"),
        Field('responsible_client', placeHolder="Responsible Client"),
        Field('tasks',css_class="custom-select", PlaceHolder="Tasks"),
        Submit('Submit', 'Submit')
    )
    class Meta:
        model = models.Project
        fields = ['title', 'responsible_client', 'tasks']
       
        

        
        
    