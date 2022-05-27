from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
