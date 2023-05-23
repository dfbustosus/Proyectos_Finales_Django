from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Individuo, Proceso, User, Partido

# Muestra Pag Principal
def index(request):
    return render(request, 'app/info_index.html')
    
def Home_registro_post(request):
    # Obtine los datos del registro del formulario
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    username=request.POST['username']
    password=request.POST['password']
    e_mail=request.POST['email']
    #Crear el usuario para la base de datos
    Usuario= User()
    Usuario.first_name=nombres
    Usuario.last_name=apellidos
    Usuario.username=username
    Usuario.email=e_mail
    Usuario.set_password(password)
    #Guarda al usuario en la base de datos
    try:
        Usuario.save()
        return render(request, 'app/UsuCreado_Exito.html')      
    except:
        veri= True
        return render(request, 'app/UsuCreado_Error.html')

@login_required
def Pag_Admin(request):
    return render(request, 'app/Pag_Admin_Style.html')

@login_required
def Pag_Usu(request):
    return render(request, 'app/Pag_Usuario_Style.html')

def Home_login_post(request):
    usu = request.POST['username']
    contra = request.POST['password']
    usuario=authenticate(username=usu, password=contra)    
    if usuario is None:
        return render(request, 'app/Error_Login.html')
    else:
        login(request, usuario)
        if request.user.is_superuser == True:
            return redirect('app:Pag_Admin')
        else:
            return redirect('app:Pag_Usu')

@login_required
def cerrar_sesion_post(request):
    logout(request)
    return redirect('app:index')


@login_required
def Actualizar_Datos_Admin(request):
    return render(request, 'app/Actualizar_Datos_Admin.html')

def Actualizar_Datos_Post(request, id_usuario):
    Update_Usu = User.objects.get(id=id_usuario) # Crea el obejeto que contiene el usurio a actualizar
    # Obtine los datos del registro del formulario
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    username=request.POST['username']
    password=request.POST['password']
    e_mail=request.POST['email']
    
    #Actualiza el usuario para la base de datos
    Update_Usu.first_name=nombres
    Update_Usu.last_name=apellidos
    Update_Usu.username=username
    Update_Usu.email=e_mail
    Update_Usu.set_password(password)
    #Guarda al usuario en la base de datos
    try:
        Update_Usu.save()        
        if Update_Usu.is_superuser == True:
            return render(request, 'app/UsuActu_Exito_Admin.html')
        else:
            return render(request, 'app/UsuActu_Exito_Usu.html')              
    except:        
        if Update_Usu.is_superuser == True:
            return render(request, 'app/UsuActu_Error_Admin.html')
        else:
            return render(request, 'app/UsuActu_Error_Usu.html')
        

@login_required
def Actualizar_Datos_Usu(request):
    return render(request, 'app/Act_Datos_Usu.html')  

@login_required
def Crear_Partido_Politico(request):
    return render(request, 'app/Crear_Partido_Politico.html') 


@login_required
def Crear_Partido_Politico_Post(request, id_usuario):
    UsuFK = User.objects.get(id=id_usuario)
    partido=request.POST['partido']
    part = Partido()
    part.nombre = partido
    part.creador = UsuFK
    part.visitas = 0
    try:  
        part.save()
        return render(request, 'app/Crear_Partido_Politico_Exito.html') 
    except:
        return render(request, 'app/Crear_Partido_Politico_Erro.html') 


# Falta ordenar por la cantidad de procesos
@login_required
def Lista_Partido(request, id_usuario):
    Usu = User.objects.get(id=id_usuario)
    Lista = Partido.objects.all()
    contexto ={
        'listas': Lista
    }
    if Usu.is_superuser == True:
        return render(request, 'app/Lista_Partidos_Admin.html',contexto)
    else:
        return render(request, 'app/Lista_Partidos_Usu.html',contexto)


    






@login_required
def Consul_Lista_Individuos_Admin(request):   
    contexto={ 
        'Nombre':'sapo',
        'lista': [
            {'Nombre':'Jonathanassss', 'Apellidos':'Guresdsfdsf'},
            {'Nombre':'nombrsioto', 'Apellidos':'apelldisos'},
        ]
        
        
    }
    return render(request, 'app/Consul_Lista_Individuos_Admin.html',contexto)


@login_required
def Lista_Individuos(request, id_usuario,):
    Usu = User.objects.get(id=id_usuario)
    Lista = Individuo.objects.all()
    #ndi=Individuo.objects.get(aprobado)
    contexto ={
        'listas': Lista
    }
    if Usu.is_superuser == True:
       return render(request, 'app/Lista_Individuos_Admin.html',contexto)
    else:
    
         return render(request, 'app/Lista_Individuos_Usu.html',contexto)







@login_required
def Consutar_PartidoP_Usuario(request):
    lista=Partido.objects.all
    contexto={
        'Consultar_PartidoP_Usuario':lista
    }
    return render(request, 'app/Consultar_PartidoP_Usuario.html')


@login_required
def Crear_Individuo_Admin(request):
    return render(request, 'app/Crear_Individuo_Admin.html') 



@login_required
def Crear_Individuo_Admin_Post(request,id_usuario):
    
    UsuFK = User.objects.get(id=id_usuario)
    apellidos=request.POST['Apellidos']
    nombres=request.POST['Nombres']
    fecha=request.POST['Fecha de Nacimiento']
    
    
    indiv= Individuo()
    indiv.apellidos = apellidos
    indiv.nombres = nombres
    indiv.creador = UsuFK
    indiv.visitas=0
    indiv.fecha_nacimineto = fecha
    if UsuFK.is_superuser == True:
        indiv.aprobado=1
    else:
        indiv.aprobado=0
    try:  
            indiv.save()
            return render(request, 'app/Crear_Individuo_Admin_Exito.html') 
    except:
        return render(request, 'app/Crear_Individuo_Error.html') 




@login_required
def Crear_Individuo_Usu(request):
    return render(request, 'app/Crear_Individuo_Usu.html') 

@login_required
def Crear_Individuo_Usu_Post(request,id_usuario):
    
    UsuFK = User.objects.get(id=id_usuario)
    apellidos=request.POST['Apellidos']
    nombres=request.POST['Nombres']
    fecha=request.POST['Fecha de Nacimiento']
    
    
    indi = Individuo()
    indi.apellidos = apellidos
    indi.nombres = nombres
    indi.creador = UsuFK
    indi.visitas=0
    indi.fecha_nacimineto = fecha
    if UsuFK.is_superuser == True:
        indi.aprobado=1
    else:
        indi.aprobado=0
    try:  
            indi.save()
            return render(request, 'app/Crear_Indivduo_Exito_Usu.html') 
    except:
        return render(request, 'app/Crear_Individuo_Error_Usu.html') 




@login_required
def Crear_Proceso_Admin(request):
    return render(request, 'app/Crear_Proceso_Admin.html') 



@login_required
def Crear_Proceso_Admin_Post(request):

    UsuFK = request.user
    titulo=request.POST['titulo']
    F_Inicio=request.POST['F_Inicio']
    F_Fin=request.POST['F_Fin']
    abierto=False
    if 'abierto' in request.POST:
        abierto=True
    entidad=request.POST['entidad']
    monto=request.POST['monto']
    comentarios=request.POST['comentarios']
    

    proce = Proceso()
    proce.titulo = titulo
    proce.fecha_inicio=F_Inicio
    proce.fecha_fin=F_Fin
    proce.abierto=abierto
    proce.entidad=entidad
    proce.monto=monto
    proce.comentarios=comentarios
    proce.creador = UsuFK
    

    if UsuFK.is_superuser == True:
        proce.aprobado=1
    else:
        proce.aprobado=0
    try:  
        proce.save()
        return render(request, 'app/Crear_Proceso_Exito.html') 
    except: 
        return render(request, 'app/Crear_Proceso_Error.html') 




@login_required
def Crear_Proceso_Usu(request):
    return render(request, 'app/Crear_Proceso_Usu.html') 



@login_required
def Crear_Proceso_Usu_Post(request,id_usuario):

    UsuFK = User.objects.get(id=id_usuario)
    titulo=request.POST['titulo']
    F_Inicio=request.POST['F_Inicio']
    F_Fin=request.POST['F_Fin']
    abierto=False
    if 'abierto' in request.POST:
        abierto=True
    entidad=request.POST['entidad']
    monto=request.POST['monto']
    comentarios=request.POST['comentarios']
    

    proce = Proceso()
    proce.titulo = titulo
    proce.fecha_inicio=F_Inicio
    proce.fecha_fin=F_Fin
    proce.abierto=abierto
    proce.entidad=entidad
    proce.monto=monto
    proce.comentarios=comentarios
    proce.creador = UsuFK
    

    if UsuFK.is_superuser == False:
        proce.aprobado=0
    else:
        proce.aprobado=1
    try:  
        proce.save()
        return render(request, 'app/Crear_Proceso_Exito_Usu.html') 
    except: 
        return render(request, 'app/Crear_Proceso_Error_Usu.html') 

