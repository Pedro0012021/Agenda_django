from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Evento(models.Model):
    titulo= models.CharField(max_length=100)
    descricao=models.TextField(null=True, blank=True)
    data_evento=models.DateTimeField()
    data_criacao=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='evento'   

    def __str__(self):
        return self.titulo     