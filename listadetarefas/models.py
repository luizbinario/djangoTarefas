from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    tarefa = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=True)