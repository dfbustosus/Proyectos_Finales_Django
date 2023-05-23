"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from appcoder.views import (AboutListar, MensajeBorrar, index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appcoder/', index, name="appcoder-index"),
    path('appcoder/<int:pk>/detalle/', PostDetalle.as_view(), name="appcoder-detalle"),
    path('appcoder/listar/', PostListar.as_view(), name="appcoder-listar"),
    path('appcoder/crear/', staff_member_required(PostCrear.as_view()), name="appcoder-crear"),
    path('appcoder/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="appcoder-borrar"),
    path('appcoder/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="appcoder-actualizar"),
    path('appcoder/signup/', UserSignUp.as_view(), name ="appcoder-signup"),
    path('appcoder/login/', UserLogin.as_view(), name= "appcoder-login"),
    path('appcoder/logout/', UserLogout.as_view(), name="appcoder-logout"),
    path('appcoder/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="appcoder-avatars-actualizar"),
    path('appcoder/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="appcoder-users-actualizar"),
    path('appcoder/mensajes/crear/', MensajeCrear.as_view(), name="appcoder-mensajes-crear"),
    path('appcoder/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="appcoder-mensajes-detalle"),
    path('appcoder/mensajes/listar/', MensajeListar.as_view(), name="appcoder-mensajes-listar"),
    path('appcoder/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="appcoder-mensajes-borrar"),
    path('appcoder/about/', AboutListar.as_view(), name= "appcoder-about"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
