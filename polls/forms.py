from django import forms
from .models import Worker


class WorkerModelForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name']