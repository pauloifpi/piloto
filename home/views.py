from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html') 

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def exibir_item(request, id):
    return render(request, 'exibir_item.html', {'id': id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})

def diasemana(request, num):

    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

    dia = dias.get(num, "Dia inválido!")

    return render(request, 'dia.html', {'dia': dia})