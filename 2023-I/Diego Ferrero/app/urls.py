from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home),
    path('about/', views.acercaDe, name='about'),
    path('agregarPost/', views.agregarPost),
    path('editar/<id>', views.editarPost),
    path('eliminar/<id>', views.eliminarPost),
    path('pages/<id>', views.verPost),
    path('imagen/<id>', views.stream_file, name='imagen'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
path('register/', views.register, name='register'),
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



