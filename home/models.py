from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING
    )

