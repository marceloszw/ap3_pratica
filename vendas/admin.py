from django.contrib import admin

from .models import Cliente, Motocicleta, Venda

admin.site.register(Cliente)
admin.site.register(Motocicleta)
admin.site.register(Venda)
