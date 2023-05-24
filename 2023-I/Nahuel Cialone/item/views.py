
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Categoria
from .forms import NewItemForm, EditItemForm
#importamos para poder realizar busquedas a fondo sobre la base de datos
from django.db.models import Q

def items(request):
    busqueda = request.GET.get('busqueda', '')
    categoria_id = request.GET.get('categoria', 0)
    categorias = Categoria.objects.all()
    items = Item.objects.filter(vendido=False)
    
    if categoria_id:
        items = items.filter(categoria_id=categoria_id)
    
    if busqueda:
        items = items.filter(Q(nombre__icontains=busqueda))
        
    return render(request, 'item/items.html',{
        'items': items,
        'busqueda': busqueda,
        'categorias': categorias,
        'categoria_id': int(categoria_id),
    })

def detalle(request, pk):
    #se pasa por parametro el id del item a buscar
    item = get_object_or_404(Item, pk=pk)
    #traemos 3 items relacionados de la misma categoria, filtrado por "no vendidos"
    items_relacionados = Item.objects.filter(categoria=item.categoria, vendido=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detalle.html',{
        'item': item,
        'items_relacionados': items_relacionados
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.creador = request.user
            item.save()
            
            return redirect('item:detalle', pk=item.id)
    else:
        form = NewItemForm()
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Nuevo item'
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, creador=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            
            return redirect('item:detalle', pk=item.id)
    else:
        form = EditItemForm(instance=item)
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Editar item'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, creador=request.user)
    item.delete()
    
    return redirect('dashboard:index')