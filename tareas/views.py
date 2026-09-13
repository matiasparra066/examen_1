from django.shortcuts import render

# Create your views here.

def lista_tareas(request):
    tareas = ["Comprar pan", "Estudiar Django", "Hacer ejercicio"]
    return render(request, 'tareas/lista.html', {'tareas': tareas})

def detalle_tarea(request, id):
    return render(request, 'tareas/detalle.html', {'id': id})