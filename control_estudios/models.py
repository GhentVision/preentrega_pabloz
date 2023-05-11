from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nac = models.DateField()
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nac = models.DateField()
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    profesion = models.CharField(max_length=128)
    bio = models.TextField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"