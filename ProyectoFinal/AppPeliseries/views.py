from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView, UpdateView
from .models import *
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
    template_name= 'AppPeliseries/peliculas/pelis_form.html'
    fields= '__all__'
    
class PeliUpdate(UpdateView):
    model=Pelicula
    template_name= 'AppPeliseries/peliculas/pelis_form.html'

    fields= '__all__'

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
    template_name= 'AppPeliseries/series/serie_detail.html'


class SerieCrear(CreateView):
    model=Serie
    template_name= 'AppPeliseries/series/serie_form.html'
    fields= '__all__'
    
class SerieUpdate(UpdateView):
    model=Serie
    template_name= 'AppPeliseries/series/serie_form.html'
    fields= '__all__'

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
    fields= '__all__'
    
class MusicaUpdate(UpdateView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_form.html'
    fields= '__all__'

class MusicaDelete(DeleteView):
    model=Musica
    template_name='AppPeliseries/musica/music_delete.html'
    success_url= reverse_lazy('Ver Series')

def acercaDe(request):
    return render(request, "AppPeliseries/acercade.html")

    
'''class InicioView(ListView):
    model= Posteos
    template_name= 'AppPeliseries/inicio.html'''