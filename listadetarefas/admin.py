from django.contrib import admin

# Register your models here.
from .models import Tarefa

def public_task(modeladmin, request, queryset):
    queryset.update(public=True)
public_task.short_description = 'Tornar a(s) tarefa(s) pública(s)'

def hide_task(modeladmin, request, queryset):
    queryset.update(public=False)
hide_task.short_description = 'Arquivar a(s) tarefa(s)'

class TarefaAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "public"]
    list_display_links = ["id", "titulo", "public"]
    actions=[public_task, hide_task]
    ordering = ["id"]

admin.site.register(Tarefa, TarefaAdmin)