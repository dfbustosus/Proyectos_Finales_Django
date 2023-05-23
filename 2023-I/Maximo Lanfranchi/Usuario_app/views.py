from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserEditForm, CustomAuthenticationForm, CustomAvatarEditForm
from django.contrib.auth.models import User
from .models import Avatar
from Usuario_app.models import UserProfile



'''
Estas son las funciones de las vistas y su funcionalidad:

login_request: Gestiona la autenticación del usuario al iniciar sesión.
register_request: Maneja el proceso de registro de un nuevo usuario.
logout_request: Permite cerrar sesión en la aplicación.
profile: Permite editar el perfil de usuario, como la información personal y la contraseña.
agregarAvatar: Maneja la subida de avatares por parte del usuario.
avatares_list: Muestra una lista de avatares asociados al usuario.
avatares_borrar: Elimina un avatar específico del usuario.
perfil_info: Muestra la información detallada del perfil de usuario.


'''




# Vista para el inicio de sesión
def login_request(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return render(request, "Usuario_app/login.html", {'form': CustomAuthenticationForm()})

    form = CustomAuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(request, "Usuario_app/login.html", {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})

    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, "Usuario_app/login.html", {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})
    login(request, user)
    return redirect('home-inicio')


# Vista para el registro de usuario
def register_request(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Usuario_app/register.html', {'form': form})


# Vista para cerrar sesión
def logout_request(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home-page')


# Vista para editar el perfil de usuario
@login_required
def profile(request):
    current_user = request.user
    profile, created = UserProfile.objects.get_or_create(user=current_user)

    if request.method != 'POST':
        initial_state = {
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'description': profile.description,
            'webpage': profile.webpage,
        }
        form = CustomUserEditForm(initial=initial_state)
    else:
        form = CustomUserEditForm(request.POST)

        if form.is_valid():
            new_user_data = form.cleaned_data
            current_user.first_name = new_user_data['first_name']
            current_user.last_name = new_user_data['last_name']
            profile.description = new_user_data['description']
            profile.webpage = new_user_data['webpage']
            current_user.email = new_user_data['email']

            current_user.save()
            profile.save()

            if new_user_data['password1']:
                current_user.set_password(new_user_data['password1'])
                current_user.save()

            return redirect('Login')

    return render(request, "Usuario_app/perfil.html", {'form': form})


# Vista para agregar un avatar
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = CustomAvatarEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('home-inicio')
    else:
        miFormulario= CustomAvatarEditForm()
    return render(request, "Usuario_app/agregarAvatar.html", {"miFormulario": miFormulario})


# Vista para ver los avatares del usuario
@login_required
def avatares_list(request):
    usuario_actual = request.user
    avatares = Avatar.objects.filter(user=usuario_actual)
    return render(request, 'Usuario_app/verAvatar.html', {'avatares': avatares})


# Vista para eliminar un avatar
@login_required
def avatares_borrar(request):
    usuario_actual = request.user
    avatares = Avatar.objects.filter(user=usuario_actual)

    if request.method == 'POST':
        avatar_id = request.POST.get('avatar_id')
        avatar = Avatar.objects.get(id=avatar_id)
        avatar.delete()
        return redirect('VerAvatares')

    return render(request, 'Usuario_app/verAvatar.html', {'avatares': avatares})


# Vista para ver la información del perfil de usuario
@login_required
def perfil_info(request):
    current_user = request.user
    profile = current_user.userprofile

    return render(request, 'Usuario_app/perfil_detalle.html', {'profile': profile})
