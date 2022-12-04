from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskCreationForm(ModelForm):
    due_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Task
        fields = ['title', 'tag', 'status', 'due_date', 'task_description']
    def __init__(self, *args, **kwargs):
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'form-control'})


