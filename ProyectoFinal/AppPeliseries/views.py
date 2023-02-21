from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

def inicio(request):
    return render(request, "AppPeliseries/inicio1.html")

#peliculas
class PeliView(ListView):
    model= Pelicula
    template_name= 'AppPeliseries/peliculas/ver_pelis.html'

class PeliDetalle(DetailView):
    
    model=Pelicula
    
    template_name= 'AppPeliseries/peliculas/pelis_detail.html'


class PeliCrear(CreateView):
    
    model=Pelicula
    form_class= PeliculaForm
    template_name= 'AppPeliseries/peliculas/pelis_form.html'
    
    
class PeliUpdate(UpdateView):
    model=Pelicula
    template_name= 'AppPeliseries/peliculas/pelis_form.html'
    form_class=PeliculaForm

class PeliDelete(DeleteView):
    model=Pelicula
    template_name='AppPeliseries/peliculas/peli_delete.html'
    success_url= reverse_lazy('Ver Peliculas')
    

#series
class SerieView(ListView):
    model= Serie
    template_name= 'AppPeliseries/series/ver_series.html'
    
class SerieDetalle(DetailView):
    model=Serie
    template_name= 'AppPeliseries/series/series_detail.html'


class SerieCrear(CreateView):
    model=Serie
    form_class=SerieForm
    template_name= 'AppPeliseries/series/serie_form.html'
    
    
class SerieUpdate(UpdateView):
    model=Serie
    template_name= 'AppPeliseries/series/serie_form.html'
    form_class=SerieForm
    

class SerieDelete(DeleteView):
    model=Serie
    template_name='AppPeliseries/series/serie_delete.html'
    success_url= reverse_lazy('Ver Series')
    
    
    
#musica
class MusicView(ListView):
    model= Musica
    template_name= 'AppPeliseries/musica/ver_musica.html'
    

class MusicaDetalle(DetailView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_detail.html'


class MusicaCrear(CreateView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_form.html'
    form_class=MusicaForm
    
class MusicaUpdate(UpdateView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_form.html'
    form_class=MusicaForm

class MusicaDelete(DeleteView):
    model=Musica
    template_name='AppPeliseries/musica/music_delete.html'
    success_url= reverse_lazy('Ver Series')

def acercaDe(request):
    return render(request, "AppPeliseries/acercade.html")

def contacto(request):
    return render(request, "AppPeliseries/contacto.html")


'''class InicioView(ListView):
    model= Posteos
    template_name= 'AppPeliseries/inicio.html'''