from django import forms
from AppPeliseries.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PeliculaForm(forms.ModelForm):
    class Meta:
       model= Pelicula
       fields= ('autor','titulo','añoestreno', 'genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    añoestreno = forms.IntegerField(label= "Año de estreno", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label= "Reseña de la pelicula:", widget=forms.Textarea(attrs={'class': 'form-control'}))

class SerieForm(forms.ModelForm):
    class Meta:
       model= Serie
       fields= ('autor','titulo','añoestreno','temporadas', 'genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    añoestreno = forms.IntegerField(label= "Año de estreno", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    temporadas = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label= "Reseña de la serie:", widget=forms.Textarea(attrs={'class': 'form-control'}))

class MusicaForm(forms.ModelForm):
    class Meta:
       model= Musica
       fields= ('autor','nombre','pais','genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	email=forms.EmailField()
	password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2= forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
 
	class Meta:
		model = User
		fields = ("username","first_name","last_name", "email", "password1", "password2")
  
class EditarUsuario(UserCreationForm):
	email = forms.EmailField(required=True)
	email=forms.EmailField()
	password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2= forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
 
	class Meta:
		model = User
		fields = ("first_name","last_name", "email", "password1", "password2")
