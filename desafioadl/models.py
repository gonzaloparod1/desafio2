from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    
class SubTarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtarea', on_delete=models.CASCADE)   
