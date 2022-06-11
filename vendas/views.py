from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.template import loader

from vendas.models import Cliente
from vendas.models import Motocicleta
from vendas.models import Venda

def index(request):
    return render(request, 'index.html')

class ClienteListView(ListView):
    model = Cliente

class MotocicletaListView(ListView):
    model = Motocicleta

class VendaListView(ListView):
    model = Venda

def venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    context = {
        'venda': venda, 
    }
    return render(request, 'vendas/venda_detalhe.html', context)