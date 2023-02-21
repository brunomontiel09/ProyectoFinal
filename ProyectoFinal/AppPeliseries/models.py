from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Pelicula(models.Model):
    autor=models.CharField(max_length=50, default="") # Ojear cuando tenga el login!!!!!!!!!!!!!
    titulo= models.CharField(max_length=50)
    añoestreno= models.IntegerField(default=0)
    duracion=models.IntegerField()
    genero= models.CharField(max_length=30)
    body=models.TextField(default="")
    def __str__(self):
        return str(self.autor) + "  |  " + str(self.titulo)
    def get_absolute_url(self):
        return reverse("Ver Peliculas")
 
    
class Serie(models.Model):
    autor=models.CharField(max_length=50, default="")
    titulo= models.CharField(max_length=50)
    añoestreno= models.IntegerField(default=0)
    cantepisodios=models.IntegerField(default=1)
    temporadas=models.IntegerField
    genero= models.CharField(max_length=30)
    body=models.TextField(default="")
    
    def __str__(self):
        return self.autor + "  |  " + str(self.titulo)
    def get_absolute_url(self):
        return reverse("Ver Series")
    
class Musica(models.Model):
    autor=models.CharField(max_length=50, default="")
    nombre= models.CharField(max_length=50)
    pais= models.CharField(max_length=40)
    genero= models.CharField(max_length=30)
    body=models.TextField(default="")
    
    def __str__(self):
        return self.autor + "  |  " + str(self.nombre)
    
    def get_absolute_url(self):
        return reverse("Ver Musica")

"""class Posteos(models.Model):
    titulo= models.CharField(max_length=255)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField(default=0)
    
    def __str__(self):
        return self.titulo + "  |  " + str(self.autor)"""
    
    
    
    