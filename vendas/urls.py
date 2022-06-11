from django.urls import path
from vendas.views import ClienteListView, MotocicletaListView, VendaListView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', ClienteListView.as_view()),
    path('motocicletas/', MotocicletaListView.as_view()),
    path('vendas/', VendaListView.as_view()),
    path('<int:venda_id>/', views.venda, name='venda'),
]