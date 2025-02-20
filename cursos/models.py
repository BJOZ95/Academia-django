from django.db import models

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLES=(
        ('admin', 'Admin'),
        ('user', 'User_normal'),
    )

    rol= models.CharField(max_length=10, choices=ROLES, default='user')

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)
    inscritos=models.ManyToManyField(User, related_name='inscritos', blank=True)

    def __str__(self):
        return self.nombre


