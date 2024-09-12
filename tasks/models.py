from django.db import models
from django.contrib.auth.models import User

# Opções de status da tarefa
STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('em_andamento', 'Em Andamento'),
    ('concluido', 'Concluído'),
]

# Model para Tarefas
class Task(models.Model):
    title = models.CharField(max_length=200)  # Título da tarefa
    description = models.TextField()  # Descrição da tarefa
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')  # Status da tarefa
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Usuário responsável pela tarefa
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação da tarefa
    updated_at = models.DateTimeField(auto_now=True)  # Data da última atualização da tarefa

    def __str__(self):
        return self.title
