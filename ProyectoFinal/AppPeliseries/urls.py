from django.urls import path
from .views import *


urlpatterns = [
    path("/inicio/", inicio, name= "Inicio1" ),
    #path("", InicioView.as_view(), name= "Inicio"),
    
    #peliculas
    path('/ver_pelis/', PeliView.as_view(), name= 'Ver Peliculas'),
    path('/crear_peli/', PeliCrear.as_view(), name= 'Crear Post Peli'),
    path('/detalle_peli/<int:pk>', PeliDetalle.as_view(), name= 'Detalle Peli'),
    path('/editar_peli/<int:pk>', PeliUpdate.as_view(), name= 'Editar Peli'),
    path('/borrar_peli/<int:pk>', PeliDelete.as_view(), name= 'Borrar Peli'),
    
    
    #Series
    path('/ver_series/', SerieView.as_view(), name= 'Ver Series'),
    path('/crear_serie/', SerieCrear.as_view(), name= 'Crear Post Serie'),
    path('/detalle_serie/<int:pk>', SerieDetalle.as_view(), name= 'Detalle Serie'),
    path('/editar_serie/<int:pk>', SerieUpdate.as_view(), name= 'Editar Serie'),
    path('/borrar_serie/<int:pk>', SerieDelete.as_view(), name= 'Borrar Serie'),
    
    
    #musica
    
    path('/ver_musica/', MusicView.as_view(), name= 'Ver Musica'),
    path('/crear_musica/', MusicaCrear.as_view(), name= 'Crear Post Musica'),
    path('/detalle_musica/<int:pk>', MusicaDetalle.as_view(), name= 'Detalle Musica'),
    path('/editar_musica/<int:pk>', MusicaUpdate.as_view(), name= 'Editar Musica'),
    path('/borrar_musica/<int:pk>', MusicaDelete.as_view(), name= 'Borrar Musica'),
    
    
    
    path('/acerca_de/', acercaDe, name= 'Acerca de'),
    
    
    
    
]
