from django.urls import path
from AppRegistros.views import *

urlpatterns = [
  path("/padre/", padre, name= "Padre"),
   path("/login/", inicioSesion, name = "Login"),

 ]

