from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoForm


# ✅ LISTA GLOBAL DE PRODUTOS
PRODUTOS = [
    {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
    {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
    {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
    {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
    {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
    {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
    {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
    {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
    {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
    {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
    {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
    {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
    {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
]


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
        1: " 1 Domingo",
        2: " 2 Segunda-feira",
        3: " 3 Terça-feira",
        4: " 4 Quarta-feira",
        5: " 5 Quinta-feira",
        6: " 6 Sexta-feira",
        7: " 7 Sábado",
    }

    dia = dias.get(num, "Dia inválido!")

    return render(request, 'dia.html', {"dia": dia})


def produto(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)

def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/formulario.html', contexto)

def detalhes_produto(request, id):
    produto = {
        'id': id,
        'nome': 'Produto ',
        'preco': '100,00',
        'descricao': 'Descrição detalhada do produto.'
    }
    return render(request, 'produto/detalhe.html', {'produto': produto})


def editar_produto(request, id):
    form = ProdutoForm(initial={
        'nome': 'Produto Exemplo',
        'preco': '999,99',
        'descricao': 'Descrição detalhada do produto exemplo.',
    })
    contexto = {
        'form': form,
        'id': id,
    }
    return render(request, 'produto/editar.html', contexto)

def excluir_produto(request, id):
    item = None

    for p in PRODUTOS:
        if p['id'] == id:
            item = p
            break

    if item is None:
        return redirect('produto')

    if request.method == 'POST':
        PRODUTOS.remove(item)
        return redirect('produto')

    return render(request, 'produto/excluir.html', {
        'item': item
    })



