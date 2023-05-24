
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import home,agregar_producto,agregar_categoria,CategoriesListView,ProductsListView,modificar_categoria,eliminar_categoria,modificar_producto,eliminar_producto,logeo,register,agregar_mensaje_contacto,ContactoListView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', logeo, name='login'),
    path('logout', LogoutView.as_view(template_name='admin_templates/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('category_create/', agregar_categoria, name='category_create'),
    path('form_contacto_create/', agregar_mensaje_contacto, name='form_contacto_create'),
    path('contacto_list/', ContactoListView.as_view(), name='contacto_lista'),
    #path('category_list/', listar_categorias, name='category_list'),
    path('category_list/', CategoriesListView.as_view(), name='category_list'),
    path('category_update/<id>/', modificar_categoria, name='category_update'),
    path('category_eliminar/<id>/', eliminar_categoria, name='category_eliminar'),
    path('product_list/', ProductsListView.as_view(), name='product_list'),
    path('product_create/', agregar_producto, name='product_create'),
    path('product_update/<id>/', modificar_producto, name='product_update'),
    path('product_eliminar/<id>/', eliminar_producto, name='product_eliminar'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)