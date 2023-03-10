from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #home
    path("/inicio/", inicio, name= "Inicio1" ),
    path("/logout/",LogoutView.as_view(template_name="AppPeliseries/logout.html"), name="Logout" ),
    path("/editar/", editarusuario, name="Editar Usuario"),
    path("/login/", inicioSesion, name = "Login"),
    path("/registro/", registro, name = "Registro"),

    #peliculas
    path('/ver_pelis/', PeliView.as_view(), name= 'Ver Peliculas'),
    path('/crear_peli/', PeliCrear.as_view(), name= 'Crear Post Peli'),
    path('/detalle_peli/<int:pk>', PeliDetalle.as_view(), name= 'Detalle Peli'),
    path('/editar_peli/<int:pk>', PeliUpdate.as_view(), name= 'Editar Peli'),
    path('/borrar_peli/<int:pk>', PeliDelete.as_view(), name= 'Borrar Peli'),
    path('/buscarpeli/', busquedapeli, name= "Buscar Peli"),
    path('/resultado/', resultadoBusqueda, name= "Resultado"),
    
    
    #Series
    path('/ver_series/', SerieView.as_view(), name= 'Ver Series'),
    path('/crear_serie/', SerieCrear.as_view(), name= 'Crear Post Serie'),
    path('/detalle_serie/<int:pk>', SerieDetalle.as_view(), name= 'Detalle Serie'),
    path('/editar_serie/<int:pk>', SerieUpdate.as_view(), name= 'Editar Serie'),
    path('/borrar_serie/<int:pk>', SerieDelete.as_view(), name= 'Borrar Serie'),
    path('/buscarpeli/', busquedaserie, name= "Buscar serie"),
    path('/resultadoS/', resultadoBusquedaS, name= "ResultadoS"),
    
    
    
    #musica
    
    path('/ver_musica/', MusicView.as_view(), name= 'Ver Musica'),
    path('/crear_musica/', MusicaCrear.as_view(), name= 'Crear Post Musica'),
    path('/detalle_musica/<int:pk>', MusicaDetalle.as_view(), name= 'Detalle Musica'),
    path('/editar_musica/<int:pk>', MusicaUpdate.as_view(), name= 'Editar Musica'),
    path('/borrar_musica/<int:pk>', MusicaDelete.as_view(), name= 'Borrar Musica'),
    path('/buscarpeli/', busquedamusica, name= "Buscar Artista"),
    path('/resultadoM/', resultadoBusquedaM, name= "ResultadoM"),
    
    
    
    path('/acerca_de/', acercaDe, name= 'Acerca de'),
    path('/contacto/', contacto, name= 'Contacto'),

    
    
    
    
]
