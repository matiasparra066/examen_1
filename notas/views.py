from django.shortcuts import render

# Create your views here.
def lista_notas(request):
    notas = ["Reunión lunes 9am", "Comprar cuaderno", "Revisar apuntes de Django"]
    return render(request, 'notas/lista.html', {'notas': notas})

def detalle_nota(request, id):
    return render(request, 'notas/detalle.html', {'id': id})