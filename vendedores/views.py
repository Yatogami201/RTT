from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.filter(vendedor=request.user)
    return render(request, 'lista.html', {'publicaciones': publicaciones})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.vendedor = request.user
            publicacion.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'form.html', {'form': form})

@login_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)
    
    return render(request, 'form.html', {'form': form})

@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, vendedor=request.user)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'confirmar_eliminar.html', {'publicacion': publicacion})

