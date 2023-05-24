from django.shortcuts import render, get_object_or_404, redirect

from .models import Receta
from .forms import RecetaForm

from django.contrib.auth.decorators import login_required

@login_required
def receta_list(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/home.html', {'recetas': recetas})

@login_required
def receta_detail(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/receta_detail.html', {'receta': receta})

@login_required
def receta_new(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.save()
            return redirect('receta-detail', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'recetas/receta_update.html', {'form': form})

@login_required
def receta_edit(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.save()
            return redirect('receta-detail', pk=receta.pk)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/receta_update.html', {'form': form})

@login_required
def receta_delete(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    receta.delete()
    return redirect('recetas-page')