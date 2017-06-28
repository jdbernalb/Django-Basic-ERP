from django.contrib import admin

# Register your models here.
from .models import  Equipo, Consumo, Ingreso, Liquidosutilitario,Compramateriales,AnticiposRegado, Operacion,GastosVarios, Despacho, Viajes_internos, Operador,Concepto_Gastos, Material, Planta_Acopio, Mina, Cliente
admin.site.register(Equipo)
admin.site.register(Liquidosutilitario)
admin.site.register(Consumo)
admin.site.register(Ingreso)
admin.site.register(Compramateriales)
admin.site.register(AnticiposRegado)
admin.site.register(Operacion)
admin.site.register(GastosVarios)
admin.site.register(Despacho)
admin.site.register(Viajes_internos)
admin.site.register(Operador)
admin.site.register(Concepto_Gastos)
admin.site.register(Material)
admin.site.register(Planta_Acopio)
admin.site.register(Mina)
admin.site.register(Cliente)