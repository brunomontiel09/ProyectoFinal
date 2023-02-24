from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def inicio(request):
    return render(request, "AppPeliseries/inicio1.html")

#Home

def acercaDe(request):
    return render(request, "AppPeliseries/acercade.html")

def contacto(request):
    return render(request, "AppPeliseries/contacto.html")

def editarusuario(request):
    
    usuario=request.user
    
    if request.method == "POST":
        
        form =EditarUsuario(request.POST)
        
        if form.is_valid():
            
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name= info["first_name"]
            usuario.last_name= info["last_name"]
            
            usuario.save()
            
            return render(request, "AppPeliseries/inicio1.html")
        
    else:
            form  = EditarUsuario(initial={
                "email":usuario.email,
                "first_name":usuario.first_name,
                "last_name":usuario.last_name,
            })
            
    return render(request,"AppPeliseries/editar.html", {"formulario1": form, "usuario": usuario}  )

def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            
            user= authenticate(username= usuario, password= contra)
            
            if user:
                login(request, user)
                
                return render(request, "AppPeliseries/inicio1.html", {'mensaje': f"{user}"})
            
        else:
            return render(request,"AppPeliseries/inicio1.html", {'mensaje': f"Datos invalidos"})
            
    else:
        form= AuthenticationForm()
    
    return render(request, "AppPeliseries/login.html", {"formulario": form})


def registro(request):
    
    if request.method == "POST":
        form =NewUserForm(request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data["username"]
            form.save()
            context= {'mensaje': "Ahora puedes iniciar sesion"}
            return render(request, "AppPeliseries/inicio1.html", context)
        
    else:
            form  = NewUserForm()
            
    return render(request,"AppPeliseries/registro.html", {"formulario1": form} )




#peliculas
class PeliView(LoginRequiredMixin, ListView):
    model= Pelicula
    template_name= 'AppPeliseries/peliculas/ver_pelis.html'

class PeliDetalle(LoginRequiredMixin,DetailView):
    
    model=Pelicula
    
    template_name= 'AppPeliseries/peliculas/pelis_detail.html'


class PeliCrear(LoginRequiredMixin, CreateView):
    
    model=Pelicula
    form_class= PeliculaForm
    template_name= 'AppPeliseries/peliculas/pelis_form.html'
    
    
class PeliUpdate(LoginRequiredMixin, UpdateView):
    model=Pelicula
    template_name= 'AppPeliseries/peliculas/pelis_form.html'
    form_class=PeliculaForm

class PeliDelete(LoginRequiredMixin, DeleteView):
    model=Pelicula
    template_name='AppPeliseries/peliculas/peli_delete.html'
    success_url= reverse_lazy('Ver Peliculas')
    
#Buscar objetos  
@login_required
def busquedapeli(request):
     return render(request, "AppPeliseries/peliculas/busquedaPosteo.html")
 
    


def resultadoBusqueda(request):
     
    if request.GET['buscar']:
        buscar = request.GET['buscar']
        pelicula= Pelicula.objects.filter(titulo__icontains=buscar)
        return render(request, "AppPeliseries/peliculas/resultado.html", {"buscar": buscar, "pelicula": pelicula})
     
    else:
          
        respuesta= " ERROR! No enviaste datos"
          
        return render(request, "AppPeliseries/peliculas/busquedaPosteo.html",{'respuesta': respuesta})
    
#series
class SerieView(LoginRequiredMixin, ListView):
    model= Serie
    template_name= 'AppPeliseries/series/ver_series.html'
    
class SerieDetalle(LoginRequiredMixin, DetailView):
    model=Serie
    template_name= 'AppPeliseries/series/series_detail.html'


class SerieCrear(LoginRequiredMixin, CreateView):
    model=Serie
    form_class=SerieForm
    template_name= 'AppPeliseries/series/serie_form.html'
    
    
class SerieUpdate(LoginRequiredMixin, UpdateView):
    model=Serie
    template_name= 'AppPeliseries/series/serie_form.html'
    form_class=SerieForm
    

class SerieDelete(LoginRequiredMixin, DeleteView):
    model=Serie
    template_name='AppPeliseries/series/serie_delete.html'
    success_url= reverse_lazy('Ver Series')
    
    #Buscar objetos  
@login_required
def busquedaserie(request):
     return render(request, "AppPeliseries/series/busquedaPosteo.html")
 

def resultadoBusquedaS(request):
     
    if request.GET['buscar']:
        buscar = request.GET['buscar']
        serie= Serie.objects.filter(titulo__icontains=buscar)
        return render(request, "AppPeliseries/series/resultado.html", {"buscar": buscar, "serie": serie})
     
    else:
          
        respuesta= " ERROR! No enviaste datos"
          
        return render(request, "AppPeliseries/series/busquedaPosteo.html",{'respuesta': respuesta})
    
#musica
class MusicView(LoginRequiredMixin, ListView):
    model= Musica
    template_name= 'AppPeliseries/musica/ver_musica.html'
    

class MusicaDetalle(LoginRequiredMixin, DetailView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_detail.html'


class MusicaCrear(LoginRequiredMixin, CreateView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_form.html'
    form_class=MusicaForm
    
class MusicaUpdate(LoginRequiredMixin, UpdateView):
    model=Musica
    template_name= 'AppPeliseries/musica/music_form.html'
    form_class=MusicaForm

class MusicaDelete(LoginRequiredMixin, DeleteView):
    model=Musica
    template_name='AppPeliseries/musica/music_delete.html'
    success_url= reverse_lazy('Ver Musica')

#Buscar objetos  
@login_required
def busquedamusica(request):
     return render(request, "AppPeliseries/musica/busquedaPosteo.html")
 
    


def resultadoBusquedaM(request):
     
    if request.GET['buscar']:
        buscar = request.GET['buscar']
        musica= Musica.objects.filter(nombre__icontains=buscar)
        return render(request, "AppPeliseries/musica/resultado.html", {"buscar": buscar, "musica": musica})
     
    else:
          
        respuesta= " ERROR! No enviaste datos"
          
        return render(request, "AppPeliseries/musica/busquedaPosteo.html",{'respuesta': respuesta})









