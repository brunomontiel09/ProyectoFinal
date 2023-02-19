from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate





def padre(request):
    return render(request, "AppRegistros/padre.html")
    


def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            
            user= authenticate(username= usuario, password= contra)
            
            if user:
                login(request, user)
                
                return render(request, "AppPeliseries/inicio.html", {'mensaje': f"Bienvenido{user}"})
            
        else:
                return render(request,"AppPeliseries/inicio.html", {'mensaje': f"Datos invalidos"})
            
    else:
        form= AuthenticationForm()
    
    return render(request, "AppRegistros/login.html", {"formulario1": form})



"""def registro(request):
    
    if request.method == "POST":
        
        form= UserCreationForm(request.form)
        
        if form.is_valid():
            
            username= form.changed_data["username"]
            
            form.save()
            return render(request, )""" #https://drive.google.com/drive/folders/1nL_VvTB1WCxIZmlCa53jMXbPuNvX3oIJ min 15:20
            