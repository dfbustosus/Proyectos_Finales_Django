from django.shortcuts import render, get_object_or_404, redirect
from django.http    import HttpResponse
from django.db.models import Q
from AppTennis.models import Torneo,Jugador,Resultado,Inscripcion
from AppTennis.forms import TorneoFormulario,JugadorFormulario,ResultadoFormulario, InscripcionFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from AppTennis.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# creo las vistas 
# vista inicio, Torneo, Jugador, Resultado

# vista para  buscar y mostrar resultados de Jugador y torneo.
# vista para registrar usuarios y logearse.
def inicio(request):
    return render(request, 'AppTennis/Inicio.html')

def torneo(request):
    return render(request, 'AppTennis/Torneo.html')

def jugador(request):
    return render(request, 'AppTennis/Jugador.html')
 
def resultado(request):
    return render(request, 'AppTennis/Resultado.html')

def novedades(request):
    return render(request, 'AppTennis/novedades.html')

def listadostorneos(request):
    return render(request, 'AppTennis/listadostorneos.html')


# vista para formularioTorneo, formularioJugador, FormularioResultdo
def torneoFormulario(request):
    if request.method == "POST":
        miFormulario = TorneoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            torneo = Torneo(nombre=informacion['nombre'], fecha_inicio=informacion['fecha_inicio'],
                            fecha_fin=informacion['fecha_fin'], cantidad_jugadores=informacion['cantidad_jugadores'])
            torneo.save()
            return render(request, "AppTennis/inicio.html")
    else:
        miFormulario = TorneoFormulario()
    
    return render(request, "AppTennis/torneoFormulario.html", {"miFormulario": miFormulario})




def jugadorFormulario(request):
    if request.method == "POST":
        miFormulario = JugadorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            jugador = Jugador(nombre=informacion['nombre'], apellido=informacion['apellido'],dni=informacion['dni'],
                              edad=informacion['edad'], telefono=informacion['telefono'], comentario=informacion['comentario'],
                              email=informacion['email'])                                                                                 
            jugador.save()
            return render(request, "AppTennis/inicio.html")
    else:
        miFormulario = JugadorFormulario()
    
    return render(request, "AppTennis/jugadorFormulario.html", {"miFormulario": miFormulario})

def resultadoFormulario(request):
    if request.method == "POST":
        miFormulario = ResultadoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            resultado = Resultado(torneo=informacion['torneo'], jugador1=informacion['jugador1'],
                                  jugador2=informacion['jugador2'], resultado=informacion['resultado'],
                                  comentario=informacion['comentario'])
            resultado.save()
            return render(request, "AppTennis/inicio.html")
    else:
        miFormulario = ResultadoFormulario()
    
    return render(request, "AppTennis/resultadoFormulario.html", {"miFormulario": miFormulario})



def inscripcionFormulario(request):
    if request.method == "POST":
        miFormulario = InscripcionFormulario(request.POST)
        if miFormulario.is_valid():
            torneo = miFormulario.cleaned_data['torneo']
            jugador = miFormulario.cleaned_data['jugador']
            inscripcion = Inscripcion.objects.create(torneo=torneo, jugador=jugador)
            return render(request, "AppTennis/novedades.html")
    else:
        miFormulario = InscripcionFormulario()
    
    return render(request, "AppTennis/inscribirse.html", {"miFormulario": miFormulario})
# vista para  buscar y mostrar resultados de Jugador y torneo.
     
def busquedatorneo(request):
     return render(request,'AppTennis/busquedaTorneo.html')
    
def buscar_torneo(request):
    consulta = request.GET.get('consulta')
    resultado = Torneo.objects.filter(nombre__icontains=consulta)
    context = {
        'resultado': resultado,
        'consulta': consulta,
            }
       
    return render(request, 'AppTennis/resultadoBusquedaTorneo.html', context)

def busquedajugador(request):
    return render(request,'AppTennis/busquedaJugador.html')

def buscar_jugador(request):
    query = request.GET.get('query')
    resultado = Jugador.objects.filter(apellido__icontains=query)
    context = {'resultado': resultado,'consulta': query}
    return render(request, 'AppTennis/resultadoBusquedaJugador.html', context)


def listadostorneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'AppTennis/listadostorneos.html', {'torneos': torneos})

def sobremi(request):
    return render(request,'AppTennis/sobremi.html')

def contactanos(request):
    return render(request,'AppTennis/contactanos.html')

def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'AppTennis/lista_jugadores.html', {'jugadores': jugadores})

def lista_inscripciones(request):
    incripcion= Inscripcion.objects.all()
    return render(request, 'AppTennis/lista_incripcion.html', {'incripcion': incripcion})


def inscribirse(request):
    return render(request,'AppTennis/inscribirse.html')

def lista_resultados(request):
    resultados= Resultado.objects.all()
    return render(request, 'AppTennis/lista_resultados.html', {'resultados': resultados})

def gestion_inscripcion(request):
    return render(request,'AppTennis/gestion_inscripcion.html')

def gestion_jugador(request):
    return render(request,'AppTennis/gestion_jugador.html')

def gestion_torneo(request):
    return render(request,'AppTennis/gestion_torneo.html')

def gestion_resultado(request):
    return render(request,'AppTennis/gestion_resultado.html')

def leerinscripcion(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "AppTennis/gestion_inscripcion.html",  {"inscripciones": inscripciones})

def leerjugador(request):
    jugador = Jugador.objects.all()
    return render(request, "AppTennis/gestion_jugador.html",  {"jugador": jugador})

def leerresultado(request):
    resultado = Resultado.objects.all()
    return render(request, "AppTennis/gestion_resultado.html",  {"resultado": resultado})

def leertorneo(request):
    torneo = Torneo.objects.all()
    return render(request, "AppTennis/gestion_torneo.html",  {"torneo": torneo})

 
 

def eliminar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, pk=inscripcion_id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('gestion_inscripcion')  # Reemplaza 'nombre_de_la_ruta_de_gestion_inscripciones' con el nombre de la ruta que apunta a la página de gestión de inscripciones

    return render(request, 'AppTennis/eliminar_inscripcion.html', {'inscripcion': inscripcion})

def editar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, pk=inscripcion_id)
    if request.method == 'POST':
        formulario = InscripcionFormulario(request.POST, instance=inscripcion)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion_inscripcion')
    else:
        formulario = InscripcionFormulario(instance=inscripcion)
    
    return render(request, 'AppTennis/editar_inscripcion.html', {'formulario': formulario})

def eliminar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('gestion_jugador') 
    return render(request, 'AppTennis/eliminar_jugador.html', {'jugador': jugador})

def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST, instance=jugador)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion_jugador')
    else:
        formulario = JugadorFormulario(instance=jugador)

    return render(request, 'AppTennis/editar_jugador.html', {'formulario': formulario})

def eliminar_torneo(request, torneo_id):
    torneo = get_object_or_404(Torneo, pk=torneo_id)
    if request.method == 'POST':
        torneo.delete()
        return redirect('gestion_torneo') 
    return render(request, 'AppTennis/eliminar_torneo.html', {'torneo': torneo})

def editar_torneo(request, torneo_id):
    torneo = get_object_or_404(Torneo, pk=torneo_id)
    if request.method == 'POST':
        formulario = TorneoFormulario(request.POST, instance=torneo)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion_torneo')
    else:
        formulario = TorneoFormulario(instance=torneo)

    return render(request, 'AppTennis/editar_torneo.html', {'formulario': formulario})

def eliminar_resultado(request, resultado_id):
    resultado= get_object_or_404(Resultado, pk=resultado_id)
    if request.method == 'POST':
        resultado.delete()
        return redirect('gestion_resultado') 
    return render(request, 'AppTennis/eliminar_resultado.html', {'resultado': resultado})

def editar_resultado(request, resultado_id):
    resultado = get_object_or_404(Resultado, pk=resultado_id)
    if request.method == 'POST':
        formulario =ResultadoFormulario(request.POST, instance=resultado)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion_resultado')
    else:
        formulario = ResultadoFormulario(instance=resultado)

    return render(request, 'AppTennis/editar_resultado.html', {'formulario': formulario})


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, "AppTennis/inicio.html", {"mensaje": f"Bienvenido '{username}'"})
            else:
                return render(request, "AppTennis/login.html", {"formulario": formulario, "mensaje": "Datos incorrectos"})
        else:
            return render(request, "AppTennis/login.html", {"formulario": formulario, "mensaje": "Formulario incorrecto"})
    else:
        formulario = AuthenticationForm()
        return render(request, "AppTennis/login.html", {"formulario": formulario})


def register(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data.get('password')
            # Guardar el usuario con la contraseña encriptada
            user = User.objects.create_user(username=username, password=password)
            
            return render(request, "AppTennis/inicio.html", {"mensaje": "Usuario creado: {{username}}"})
    else:
        formulario = UserRegisterForm()
    
    return render(request, "AppTennis/registro.html", {"formulario": formulario})



def editarperfil(request):
    usuario=request.user
    if request.method=="POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.last_name=informacion['last_name']
            usuario.first_name=informacion['first_name']
            usuario.save()
            return render(request,"AppTennis/inicio.html" )
    else:
        miFormulario=UserEditForm(initial={'email':usuario.email})
    return render(request,"AppTennis/editar_perfil.html", {"miFormulario": miFormulario,"usuario":usuario})

