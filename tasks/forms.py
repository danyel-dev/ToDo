from django import forms
from django.forms import fields
from django import forms

from .models import task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = task
        fields = ('title', 'description')
