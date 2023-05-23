# Global Tech

## Video Explicativo 
https://youtu.be/u9woRLqtL54

## Deploy 
https://tinchotamola.pythonanywhere.com/

## Para correrlo 
* pip install -r requirements.txt
* django == 4.1.7
* pillow
* django-admin-interface
* django-crispy-forms
* crispy-bootstrap5  

Hará las siguientes funciones:
* Acciones CRUD con los productos y en las marcas
* Buscar productos en la pagina
* Registrar productos y marcas a la base
* Carrito de compras con contexto global

![](/s2.jpeg)


## Partes
1. Rutas
   1. Inicio
   2. Productos
      1. Crear
      2. Listar
      3. Actualizar
      4. Borrar
   3. Marcas
      1. Crear
      2. Actualizar
      3. Borrar
    3. Contacto 
      1. Crear 

2. Plantillas
   1. Tienda
      1. base(Nav , footer)
      2. home
      3. galeria
      4. contacto
      5. Sobre mi
   2. Producto
      1. agregar
      2. listar
      3. modificar
      4. eliminar
   2. Marca
      1. agregar
      2. listar
      3. modificar
      4. eliminar
      
3. Modelos
   1. Marca
   2. Producto
   3. Contacto
   4. Perfil

4. Vistas
   1. Tienda
      1. agregar
      2. listar
      3. actualizar
      4. eliminar
   2. Contactos
      1. enviar

5. Formularios
   1. Crear Contacto
   2. Agregar Producto
   3. Editar Producto
   4. Agregar Marca

## Pasos
1. Creo La app con Django

2. Migro las tablas

```python manage.py makemigration```
```python manage.py migrate```

4. Creo el directorio templates

5. Creo la aplicacion tienda con ```python manage.py startapp [nombre]```

6. Añado las aplicaciones a la lista de aplicaciones instaladas en settings.py

7. Verifico que se han instalado correctamente con ```python manage.py check [nombre]```
8. Creo la carpeta static para guardar todos los archivos estáticos.

10. Incluyo las urls de las aplicaciones al urls.py del proyecto

11. Añado una ruta '' para el index.html (la página principal)

12. Creo urls.py en las aplicaciones

13. Diseño el html general del proyecto

14. Defino la vista de index.html

15. Empezaremos trabajando en los productos:
    1.  Defino las rutas
    2.  Creo los modelos
    3.  Defino las vistas
    4.  Creo el formulario para crear y actualizar productos
        1.  Creo forms.py
        2.  Defino el formulario
    5. Sigo creando las vistas

16. Hago lo mismo para los otros modelos.