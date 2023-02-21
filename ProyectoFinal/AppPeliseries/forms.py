from django import forms
from AppPeliseries.models import *
from django.contrib.auth.models import User



class PeliculaForm(forms.ModelForm):
    class Meta:
       model= Pelicula
       fields= ('autor','titulo','añoestreno','duracion', 'genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    añoestreno = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    duracion = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class SerieForm(forms.ModelForm):
    class Meta:
       model= Serie
       fields= ('autor','titulo','añoestreno','cantepisodios', 'temporadas', 'genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    añoestreno = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cantepisodios = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    temporadas = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class MusicaForm(forms.ModelForm):
    class Meta:
       model= Musica
       fields= ('autor','nombre','pais','genero', 'body')
       
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

