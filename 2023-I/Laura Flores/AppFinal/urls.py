from django.urls import path
from AppFinal.views import index, about, Comentarios, ListViewRecipes, DetailViewRecipes, LogInClient, SignUpClient, UpdateClient, LogOutClient, ProfileClient, dummy, busqueda_recetas,comentariofallido, addWishlist, wishlist, CreateRecipe, DeleteRecipe, UpdateRecipe
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', index, name = "Index"),
    path ('about/', about, name= "About"),
    path ('comentarios/', Comentarios, name = "Comentarios"),
    path ('recetas/', ListViewRecipes.as_view(), name = "Recetas"),
    path ('detallerecetas/<int:pk>/', DetailViewRecipes.as_view(), name="DetalleRecetas" ),
    path ('nuevaReceta/', CreateRecipe.as_view(), name = "NuevaReceta"),
    path ('eliminarReceta/<int:pk>/', DeleteRecipe.as_view(), name = "EliminarReceta"),
    path ('actualizarReceta/<int:pk>/', UpdateRecipe.as_view(), name = "ActualizarReceta"),
    path ('busqueda/',  busqueda_recetas , name="Busqueda"),
    path ('comentariofallido/', comentariofallido),
    path ("Iniciar-sesion/", LogInClient.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", SignUpClient.as_view(), name = "Registrarse"),
    path ("actualizar/<int:pk>/", UpdateClient.as_view(), name = "Actualizar"),
    path ("Cerrar-Sesion/", LogOutClient.as_view(), name= "CerrarSesion"),
    path ("perfil/<int:pk>/", ProfileClient.as_view(), name= "Perfil"),
    path ('dummy', dummy, name= "dummy"),
    path ("addWishlist/<int:id>/", addWishlist, name = "user_wishlist"),
    path ("wishlist/", wishlist, name = "WishList")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)