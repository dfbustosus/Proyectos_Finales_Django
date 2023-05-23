# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable, Avatar
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm, BusquedaForm,AvatarFormulario
from datetime import date
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse


@login_required(login_url='Home')
def index(request):
    cursos = Curso.objects.all()
    entregables = Entregable.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    return render(request, 'index.html', {'cursos': cursos, 'entregables': entregables, 'estudiantes': estudiantes, 'profesores': profesores})


@login_required(login_url='Home')
def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Verificar si el curso ya existe en la base de datos
            nombre = form.cleaned_data['nombre']
            tipo = form.cleaned_data['Tipo']
            jornada = form.cleaned_data['Jornada']
            if Curso.objects.filter(nombre=nombre, Tipo=tipo, Jornada=jornada).exists():
                error_message = "Este curso ya está registrado."
                messages.error(request, error_message)
            else:
                form.save()
                success_message = "El curso ha sido agregado correctamente."
                messages.success(request, success_message)
                return redirect('index')
        else:
            error_message = "Por favor, complete correctamente el formulario."
            messages.error(request, error_message)
            form = CursoForm()
    else:
        form = CursoForm()

    tipos = Curso.TIPO_CHOICES
    jornadas = Curso.JORNADA_CHOICES
    return render(request, 'agregar_curso.html', {'form': form, 'tipos': tipos, 'jornadas': jornadas})



@login_required(login_url='Home')
def agregar_estudiante(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de Estudiante
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Verificar si el estudiante ya existe en el curso
            curso_id = form.cleaned_data['curso']
            Documento = form.cleaned_data['Documento']
            if Estudiante.objects.filter(Documento=Documento, curso_id=curso_id).exists():
                error_message = "Este estudiante ya está registrado en este curso."
                messages.error(request, error_message)
                return redirect('agregar_estudiante')
            
            # Guardar el formulario y crear el objeto Estudiante
            estudiante = form.save()
            messages.success(request, 'El estudiante ha sido agregado correctamente.')
            return redirect('index')
        else:
            error_message = "Por favor, complete correctamente el formulario."
            messages.error(request, error_message)
            form = EstudianteForm()
    else:
        form = EstudianteForm()
    
    cursos = Curso.objects.all()
    return render(request, 'agregar_estudiante.html', {'cursos': cursos, 'form': form})

from django.contrib import messages

@login_required(login_url='Home')
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            documento = form.cleaned_data['Documento']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            curso = form.cleaned_data['curso']

            # Verificar si el profesor ya existe en ese curso
            existe = Profesor.objects.filter(
                Documento=documento, curso=curso).exists()
            if existe:
                message = "El profesor ya existe en ese curso."
                cursos = Curso.objects.all()
                return render(request, 'agregar_profesor.html', {'cursos': cursos, 'message': message, 'form': form})

            # Si el profesor no existe, crearlo
            profesor = Profesor(nombre=nombre, apellido=apellido,
                                Documento=documento, email=email, curso=curso)
            profesor.save()

            
            messages.success(request, 'El profesor ha sido agregado exitosamente.')

            return redirect('index')
        else:
            
            messages.error(request, 'Por favor, complete el formulario correctamente.')
    else:
        form = ProfesorForm()
    
    cursos = Curso.objects.all()
    return render(request, 'agregar_profesor.html', {'cursos': cursos, 'form': form})




@login_required(login_url='Home')
def agregar_entregable(request):
    fecha_actual = date.today()
    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()

    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            entregable = form.save(commit=False)
            archivo_adjunto = form.cleaned_data.get('archivo')
            # se guarda el archivo en MEDIA_ROOT y solo guardamos el nombre del archivo en el campo de archivo
            entregable.archivo.name = archivo_adjunto.name
            entregable.fecha_entrega = timezone.now()
            entregable.save()
            form.save_m2m()

            success_message = "El Entregable ha sido agregado correctamente."
            messages.success(request, success_message)

            return redirect('index')
        else:
            error_message = "Por favor, completa correctamente el formulario."
            messages.error(request, error_message)
    else:
        form = EntregableForm()

    return render(request, 'agregar_entregable.html', {'form': form, 'cursos': cursos, 'estudiantes': estudiantes, 'fecha_actual': fecha_actual})


from django.contrib import messages

@login_required(login_url='Home')
def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            opcion_busqueda = form.cleaned_data['opcion']
            termino_busqueda = form.cleaned_data['busqueda']
            if opcion_busqueda == 'curso':
                resultados = Curso.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_curso', args=[resultado.id])
            elif opcion_busqueda == 'estudiante':
                resultados = Estudiante.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_estudiante', args=[resultado.id])
            elif opcion_busqueda == 'profesor':
                resultados = Profesor.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_profesor', args=[resultado.id])
            elif opcion_busqueda == 'entregable':
                resultados = Entregable.objects.filter(titulo__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_entregable', args=[resultado.id])
            elif opcion_busqueda == 'todos_los_cursos':
                resultados = Curso.objects.all()
                termino_busqueda = "curso"
                for resultado in resultados:
                    resultado.url = reverse('detalle_curso', args=[resultado.id])
            else:
                resultados = []
                messages.error(request, "Por favor, ingresa un término de búsqueda.")
                form = BusquedaForm() 

                return render(request, 'buscar.html', {'form': form, 'resultados': resultados, 'termino_busqueda': termino_busqueda})
                
            mensajes = messages.get_messages(request)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda, 'opcion_busqueda': opcion_busqueda, 'mensajes': mensajes})
    else:
        form = BusquedaForm()

    mensajes = messages.get_messages(request)
    return render(request, 'buscar.html', {'form': form, 'mensajes': mensajes})



@login_required(login_url='Home')
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST)
        entregable_form = EntregableForm(request.POST)
        profesor_form = ProfesorForm(request.POST)
        
        if estudiante_form.is_valid() and entregable_form.is_valid() and profesor_form.is_valid():
            # Guardar los datos del estudiante
            estudiante = estudiante_form.save(commit=False)
            estudiante.curso = curso
            estudiante.save()
            
            # Guardar los datos del entregable
            entregable = entregable_form.save(commit=False)
            entregable.curso = curso
            entregable.save()
            
            # Guardar los datos del profesor
            profesor = profesor_form.save(commit=False)
            profesor.curso = curso
            profesor.save()
            
            
            return redirect('nombre_de_la_vista')
    else:
        estudiante_form = EstudianteForm()
        entregable_form = EntregableForm()
        profesor_form = ProfesorForm()

    context = {
        'curso': curso,
        'estudiante_form': estudiante_form,
        'entregable_form': entregable_form,
        'profesor_form': profesor_form
    }

    return render(request, 'detalle_curso.html', context)




@login_required(login_url='Home')
def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    entregables = Entregable.objects.filter(estudiante=estudiante)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante, 'entregables': entregables})

def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    cursos = Curso.objects.filter(profesor__Documento=profesor.Documento)
    context = {'profesor': profesor, 'cursos': cursos}
    return render(request, 'detalle_profesor.html', context)


@login_required(login_url='Home')
def detalle_entregable(request, entregable_id):
    entregable = get_object_or_404(Entregable, id=entregable_id)
    return render(request, 'detalle_entregable.html', {'entregable': entregable})


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'El usuario ya existe')
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    form.add_error(
                        'password2', 'Las contraseñas no coinciden')
                else:
                    form.save()
                    username = form.cleaned_data['username']
                    messages.success(request, f'Usuario {username} creado correctamente')
                    return redirect('Home')
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user}')
                return redirect('index')
            else:
                return render(request, "login.html", {"Mensaje": "Error, datos ingresados incorrectos"})
        else:
            return render(request, "login.html", {"Mensaje": "Datos ingresados incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})


def Home(request):
    return render(request, "Home.html")


def logout_view(request):
    logout(request)
    messages.info(
        request, 'Has cerrado la sesión exitosamente. ¡Hasta luego!')
    return redirect('Home')


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            password1 = informacion['password1']
            password2 = informacion['password2']
            if password1 == password2:
                # Actualizar la contraseña utilizando set_password
                usuario.set_password(password1)
            else:
                miFormulario.add_error(
                    'password2', 'Las contraseñas no coinciden')
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()
            return render(request, 'index.html')
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, 'editarPerfil.html', {'miFormulario': miFormulario, 'usuario': usuario})


def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request,'index.html',{"url":avatares[-1].imagen.url})

def moatrarAvatar(request):
    user = Avatar.objects.get(user=request.user)
    return render(request, 'editarPerfilhtml', {'user_avatar': user})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            # Verificar si ya existe un avatar para el usuario
            if Avatar.objects.filter(user=u).exists():
                # Si existe, eliminar el avatar anterior
                avatar_anterior = Avatar.objects.get(user=u)
                avatar_anterior.delete()
            # Agregar el nuevo avatar
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "index.html")
    else:
        miFormulario = AvatarFormulario()
    return render(request, "editar_avatar.html", {"miFormulario": miFormulario})


def about_me(request):
    nombre = "Joaquin Sanabria"
    foto = "static/img/mifoto.jpg"
    descripcion = "35 años"
    estudios = "Ing.Eletrotecnia , Data Analaytics , Estudiante de Data Scientist y Python en Coder House"
    proyecto = "Pagina desarrollada con Django. Para el curso de Python en Coder House "

    return render(request, 'about_me.html', {'nombre': nombre, 'foto': foto, 'descripcion': descripcion, 'estudios': estudios, 'proyecto': proyecto})

