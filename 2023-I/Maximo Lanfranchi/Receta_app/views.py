from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from .forms import RecetaForm
from django.contrib.auth.decorators import login_required


@login_required
def receta_list(request):
    # Obtener todas las recetas
    recetas = Receta.objects.all()
    return render(request, 'Receta_app/receta_pages.html', {'recetas': recetas})


@login_required
def receta_detail(request, pk):
    # Obtener una receta específica por su clave primaria (id)
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'Receta_app/receta_detalle.html', {'receta': receta})


@login_required
def receta_modificar(request, pk):
    # Obtener una receta específica por su clave primaria (id)
    receta = get_object_or_404(Receta, pk=pk)
    
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        
        if form.is_valid():
            # Guardar los cambios en la receta
            receta = form.save(commit=False)
            receta.save()
            return redirect('receta-detalle', pk=receta.pk)
    else:
        form = RecetaForm(instance=receta)
    
    return render(request, 'Receta_app/receta_modificar.html', {'form': form})


@login_required
def receta_nuevo(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Guardar la nueva receta
            receta = form.save(commit=False)
            receta.save()
            return redirect('receta-detalle', pk=receta.pk)
    else:
        form = RecetaForm()
    
    return render(request, 'Receta_app/receta_modificar.html', {'form': form})


@login_required
def confirmar_receta_borrar(request, pk):
    # Obtener una receta específica por su clave primaria (id)
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'Receta_app/receta_borrar.html', {'receta': receta})


@login_required
def receta_borrar(request, pk):
    # Obtener una receta específica por su clave primaria (id) y eliminarla
    receta = get_object_or_404(Receta, pk=pk)
    receta.delete()
    return redirect('receta_list')


@login_required
def about(request):
    # Renderizar la página "aboutme.html"
    return render(request, 'Receta_app/aboutme.html')


@login_required
def contact(request):
    # Renderizar la página "contacto.html"
    return render(request, 'Receta_app/contacto.html')


@login_required
def receta_buscar(request):
    if request.method == 'GET':
        author_query = request.GET.get('author')  # Obtener el valor del parámetro 'author' del formulario

        if author_query:
            # Filtrar las recetas por el autor especificado
            recetas = Receta.objects.filter(author__icontains=author_query)

        else:
            recetas = []

        return render(request, 'Receta_app/receta_buscar.html', {'recetas': recetas})

    return redirect('receta_list')
