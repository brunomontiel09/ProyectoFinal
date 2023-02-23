from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Pelicula(models.Model):
    autor=models.CharField(max_length=50, default="") # Ojear cuando tenga el login!!!!!!!!!!!!!
    titulo= models.CharField(max_length=50)
    image= models.ImageField(null=True, blank=True,upload_to="images/pelis/")
    añoestreno= models.IntegerField(blank=True)
    genero= models.CharField(max_length=30)
    reseña=models.TextField(default="")
    def __str__(self):
        return str(self.autor) + "  |  " + str(self.titulo)
    def get_absolute_url(self):
        return reverse("Ver Peliculas")
 
    
class Serie(models.Model):
    autor=models.CharField(max_length=50, default="")
    titulo= models.CharField(max_length=50)
    image= models.ImageField(null=True, blank=True,upload_to="images/series/")
    añoestreno= models.IntegerField(default=0)
    cantepisodios=models.IntegerField(default=1)
    temporadas=models.IntegerField(default=1)
    genero= models.CharField(max_length=30)
    reseña=models.TextField(default="")
    
    def __str__(self):
        return self.autor + "  |  " + str(self.titulo)
    def get_absolute_url(self):
        return reverse("Ver Series")
    
class Musica(models.Model):
    autor=models.CharField(max_length=50, default="")
    image= models.ImageField(null=True, blank=True,upload_to="images/musica/")
    nombre= models.CharField(max_length=50)
    pais= models.CharField(max_length=40)
    genero= models.CharField(max_length=30)
    reseña=models.TextField(default="")
    
    def __str__(self):
        return self.autor + "  |  " + str(self.nombre)
    
    def get_absolute_url(self):
        return reverse("Ver Musica")


    
    
    
    