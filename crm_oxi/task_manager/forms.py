from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter task description here...',
                'rows': 3 
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title here...',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Remove the labels for the fields
        self.fields['description'].label = ''