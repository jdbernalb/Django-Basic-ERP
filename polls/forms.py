# -*- coding: utf-8 -*-
from django.forms import ModelForm,forms
from .models import  Consumo, Ingreso, Liquidosutilitario,Compramateriales,AnticiposRegado, Operacion,GastosVarios, Despacho, Viajes_internos
from django.contrib.admin import widgets  
from datetime import datetime
# Create your models here.

class CompramaterialesForm(ModelForm):
    class Meta:
        model = Compramateriales
        fields = [ 'pub_modified', 'nombre_material','costo']
    def __init__(self, *args, **kwargs):
        super(CompramaterialesForm, self).__init__(*args, **kwargs)
        self.fields['nombre_material'].label = "Nombre Material"
        self.fields['pub_modified'].label = "Fecha de Compra"
        self.fields['costo'].label = "Costo Material"
        

    def save(self, commit=True):
        compramaterialesForm = super(CompramaterialesForm, self).save(commit=False)
        compramaterialesForm.pub_date = datetime.now()
        compramaterialesForm.save()
        return compramaterialesForm


class OperacionForm(ModelForm):
    class Meta:
        model = Operacion
        fields = [ 'tipo_operacion', 'nombre_equipo', 'nombre_operador','pub_modified', 'porcentaje_dedicado','horometro_inicial','horometro_final']
    def __init__(self, *args, **kwargs):
        super(OperacionForm, self).__init__(*args, **kwargs)
        self.fields['tipo_operacion'].label = "Seleccione"
        self.fields['nombre_equipo'].label = "Nombre Equipo"
        self.fields['nombre_operador'].label = "Operador"
        self.fields['pub_modified'].label = "Fecha de Operación"
        self.fields['porcentaje_dedicado'].label = "Porcentaje Dedicado (%)"
        self.fields['horometro_inicial'].label = "Horometro Inicial"
        self.fields['horometro_final'].label = "Horometro Final"

    def save(self, commit=True):
        operacionForm = super(OperacionForm, self).save(commit=False)
        operacionForm.pub_date = datetime.now()
        operacionForm.save()
        return operacionForm



class AnticiposRegadoForm(ModelForm):
    class Meta:
        model = AnticiposRegado
        fields = [ 'pub_modified', 'tipo_operacion','nombre_equipo','cantidad']


    def __init__(self, *args, **kwargs):
        super(AnticiposRegadoForm, self).__init__(*args, **kwargs)
        self.fields['tipo_operacion'].label = "Seleccione"
        self.fields['pub_modified'].label = "Fecha de Compra"
        self.fields['nombre_equipo'].label = "Nombre Equipo"
        

    def save(self, commit=True):
        anticiposRegadoForm = super(AnticiposRegadoForm, self).save(commit=False)
        anticiposRegadoForm.pub_date = datetime.now()
        anticiposRegadoForm.save()
        return AnticiposRegadoForm

class ConsumoForm(ModelForm):
    class Meta:
        model = Consumo
        fields = ['nombre_liquido', 'nombre_equipo', 'pub_modified', 'total_galones']
    def __init__(self, *args, **kwargs):
        super(ConsumoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_liquido'].label = "Nombre Líquido"
        self.fields['nombre_equipo'].label = "Nombre Equipo"
        self.fields['pub_modified'].label = "Fecha de Consumo"
        self.fields['total_galones'].label = "Galones Consumidos"
        

    def save(self, commit=True):
        consumoform = super(ConsumoForm, self).save(commit=False)
        consumoform.pub_date = datetime.now()
        l = Liquidosutilitario.objects.get(nombre_liquido=consumoform.nombre_liquido)
        consumoform.precio_liquido = l.precio_liquido
        consumoform.inv_inicial = l.inventario 
        consumoform.inv_final = l.inventario - consumoform.total_galones
        l.inventario = consumoform.inv_final
        l.save()
        consumoform.save()
        return consumoform

class IngresoForm(ModelForm):
    class Meta:
        model = Ingreso
        fields = ['nombre_liquido', 'precio_liquido','pub_modified', 'total_galones']
    def __init__(self, *args, **kwargs):
        super(IngresoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_liquido'].label = "Nombre Liquido"
        self.fields['precio_liquido'].label = "Precio"
        self.fields['pub_modified'].label = "Fecha de Ingreso"
        self.fields['total_galones'].label = "Galones Ingresados"
        

    def save(self, commit=True):
        ingresoForm = super(IngresoForm, self).save(commit=False)
        ingresoForm.pub_date = datetime.now()
        l = Liquidosutilitario.objects.get(nombre_liquido=ingresoForm.nombre_liquido)
        ingresoForm.inv_inicial = l.inventario
        ingresoForm.inv_final = l.inventario + ingresoForm.total_galones
        l.inventario = consumoform.inv_final
        l.save()
        ingresoForm.save()
        return ingresoForm



class GastosVariosForm(ModelForm):
    class Meta:
        model = GastosVarios
        fields = ['concepto_gastos','pub_modified', 'total']
    def __init__(self, *args, **kwargs):
        super(GastosVariosForm, self).__init__(*args, **kwargs)
        self.fields['concepto_gastos'].label = "Seleccione"
        self.fields['pub_modified'].label = "Fecha de Gasto"
        self.fields['total'].label = "Total"
        

    def save(self, commit=True):
        gastosVariosForm = super(GastosVariosForm, self).save(commit=False)
        gastosVariosForm.pub_date = datetime.now()
        gastosVariosForm.save()
        return ingresoForm


class DespachoForm(ModelForm):
    class Meta:
        model = Despacho
        fields = ['pub_modified', 'planta_Acopio', 'nombre_equipo' ,'nombre_material','numero_factura','nombre_cliente','peso_entrada_1','peso_entrada_2','peso_entrada_3','peso_salida_1','peso_salida_2','peso_salida_3']
    def __init__(self, *args, **kwargs):
        super(DespachoForm, self).__init__(*args, **kwargs)
        self.fields['pub_modified'].label = "Fecha de Despacho"
        self.fields['planta_Acopio'].label = "Planta de Acopio"
        self.fields['nombre_equipo'].label = "Nombre Equipo"
        self.fields['nombre_material'].label = "Nombre Material"
        self.fields['nombre_cliente'].label = "Nombre Cliente"
        self.fields['numero_factura'].label = "Número de Factura"
        self.fields['peso_entrada_1'].label = "Peso de Entrada 1"
        self.fields['peso_entrada_2'].label = "Peso de Entrada 2"
        self.fields['peso_entrada_3'].label = "Peso de Entrada 3"
        self.fields['peso_salida_1'].label = "Peso de Salida 1"
        self.fields['peso_salida_2'].label = "Peso de Salida 1"
        self.fields['peso_salida_3'].label = "Peso de Salida 1"
        

    def save(self, commit=True):
        despachoForm = super(DespachoForm, self).save(commit=False)
        despachoForm.pub_date = datetime.now()
        despachoForm.save()
        return despachoForm

class Viajes_internosForm(ModelForm):
    class Meta:
        model = Viajes_internos
        fields = [ 'pub_modified', 'destino','nombre_equipo','mina','cantidad']


    def __init__(self, *args, **kwargs):
        super(Viajes_internosForm, self).__init__(*args, **kwargs)
        self.fields['pub_modified'].label = "Fecha de Viaje"
        self.fields['destino'].label = "Destino"
        self.fields['nombre_equipo'].label = "Nombre Equipo"
        self.fields['mina'].label = "Mina"
        self.fields['cantidad'].label = "Cantidad"
        

    def save(self, commit=True):
        viajes_internosForm = super(Viajes_internosForm, self).save(commit=False)
        viajes_internosForm.pub_date = datetime.now()
        viajes_internosForm.save()
        return viajes_internosForm