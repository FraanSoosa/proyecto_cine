from django.db import models


class Peliculas(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    sala = models.CharField(max_length=30)

class Sala(models.Model):
    number = models.IntegerField()
    code = models.IntegerField()
    

class Promociones(models.Model):
    precio = models.IntegerField()
    code = models.IntegerField()
    descripcion = models.CharField(max_length=500)

class Schedule(models.Model):
    horario = models.DateField()
    pelicula = models.CharField(max_length=40)
    sala = models.IntegerField()
    code = models.IntegerField()
    # pelicula = models.OneToOneField(Peliculas, on_delete=models.CASCADE) ==> buscar django relational fields
    # Ono-to-One//One-to-Many//Many-To-Many
    