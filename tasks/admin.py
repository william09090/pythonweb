from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to', 'created_at')  # Exibe as colunas no admin

    list_filter = ('status',)  # Adiciona o filtro pelo campo status

admin.site.register(Task)       # Registre o modelo Task
