from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm, DesarrolloForm, EstadoTareaForm, TareaSearchForm

def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tarea_list.html', {'tareas': tareas})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_form.html', {'form': form})

def desarrollo_create(request):
    if request.method == 'POST':
        form = DesarrolloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = DesarrolloForm()
    return render(request, 'tareas/desarrollo_form.html', {'form': form})

def estado_create(request):
    if request.method == 'POST':
        form = EstadoTareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = EstadoTareaForm()
    return render(request, 'tareas/estado_form.html', {'form': form})

def tarea_search(request):
    form = TareaSearchForm(request.GET)
    tareas = Tarea.objects.all()
    
    if form.is_valid():
        search = form.cleaned_data['search']
        if search:
            tareas = tareas.filter(nombre__icontains=search)
    
    return render(request, 'tareas/tarea_list.html', {'tareas': tareas, 'form': form})