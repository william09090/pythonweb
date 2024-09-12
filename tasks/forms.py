from django import forms
from .models import Task

# Formulário para Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Referência ao modelo Task
        fields = ['title', 'description', 'status', 'assigned_to']  # Campos disponíveis no formulário
        widgets = {
            'status': forms.Select(),  # O Django automaticamente usa as choices do modelo Task
        }
