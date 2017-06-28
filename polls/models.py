# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

OP_CHOICES = (
    ('D', 'Dragado'),
    ('E', 'Explotacion'),
	('R', 'Recuperacion'),
)
AR_CHOICES = (
    ('An', 'Anticipo'),
    ('Re', 'Regado'),
)

def validate_percentage(value):
    if (value > 100) | (0 > value):
        raise ValidationError(
            _('%(value)s no está permitido'),
            params={'value': value},
        )

class Equipo(models.Model):
	nombre_equipo = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_equipo
class Operador(models.Model):
	nombre_operador = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_operador
class Liquidosutilitario(models.Model):
	nombre_liquido = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	precio_liquido = models.IntegerField()
	pub_modified = models.DateTimeField('date modified')
	inventario = models.IntegerField()
	def was_price_updated_recently(self):
		return self.pub_modified >= timezone.now() - datetime.timedelta(month=1)
	def __str__(self):
		return self.nombre_liquido
class Concepto_Gastos(models.Model):
	concepto = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.concepto
class Material(models.Model):
	nombre_material = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_material
class Planta_Acopio(models.Model):
	nombre_planta = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_planta
class Mina(models.Model):
	nombre_mina = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_mina
class Cliente(models.Model):
	nombre_cliente = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.nombre_cliente


class Compramateriales(models.Model):
	pub_date = models.DateTimeField('date published')
	pub_modified = models.DateTimeField('date modified')
	nombre_material = models.ForeignKey(Material, on_delete=models.CASCADE)
	costo = models.IntegerField()	
	def __str__(self):
		return str(self.id)
class AnticiposRegado(models.Model):
	pub_date = models.DateTimeField('date published')
	pub_modified = models.DateTimeField('date modified')
	tipo_operacion = models.CharField(max_length=2, choices=AR_CHOICES)
	nombre_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
	cantidad = models.IntegerField()	
	def __str__(self):
		return str(self.id)
class Operacion(models.Model):
	pub_date = models.DateTimeField('date published')
	tipo_operacion = models.CharField(max_length=3, choices=OP_CHOICES)
	nombre_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
	nombre_operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
	pub_modified = models.DateTimeField('date modified')
	porcentaje_dedicado = models.IntegerField(validators=[validate_percentage])
	horometro_inicial = models.IntegerField()
	horometro_final = models.IntegerField()
	operacion_id = models.IntegerField()
	def __str__(self):
		return sstr(self.id)

class Consumo(models.Model):
	nombre_liquido = models.ForeignKey(Liquidosutilitario)
	nombre_equipo = models.ForeignKey(Equipo)
	pub_date = models.DateTimeField('date published')
	precio_liquido = models.IntegerField()
	pub_modified = models.DateField('date modified')
	inv_inicial = models.IntegerField()
	total_galones = models.IntegerField()
	inv_final = models.IntegerField()
	def __str__(self):
		return str(self.id)
class GastosVarios(models.Model):
	concepto_gastos = models.ForeignKey(Concepto_Gastos) 
	pub_date = models.DateTimeField('date published')
	pub_modified = models.DateField('date modified')
	total = models.IntegerField()
	def __str__(self):
		return str(self.id)
class Ingreso(models.Model):
	nombre_liquido = models.ForeignKey(Liquidosutilitario)
	pub_date = models.DateTimeField('date published')
	precio_liquido = models.IntegerField()
	pub_modified = models.DateField('date modified')
	inv_inicial = models.IntegerField()
	total_galones = models.IntegerField()
	inv_final = models.IntegerField()
	def __str__(self):
		return str(self.id)
class Despacho(models.Model):
	pub_date = models.DateTimeField('date published')
	pub_modified = models.DateField('date modified')
	planta_Acopio = models.ForeignKey(Planta_Acopio)
	nombre_equipo = models.ForeignKey(Equipo)
	nombre_material = models.ForeignKey(Material, on_delete=models.CASCADE)
	numero_factura = models.IntegerField()
	nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	peso_entrada_1=models.IntegerField()
	peso_entrada_2=models.IntegerField()
	peso_entrada_3=models.IntegerField()
	peso_salida_1=models.IntegerField()
	peso_salida_2=models.IntegerField()
	peso_salida_3=models.IntegerField()
	def __str__(self):
		return str(self.id)
class Viajes_internos(models.Model):
	pub_date = models.DateTimeField('date published')
	pub_modified = models.DateField('date modified')
	destino = models.ForeignKey(Planta_Acopio)
	nombre_equipo = models.ForeignKey(Equipo)
	mina = models.ForeignKey(Mina)
	cantidad = models.IntegerField()
	def __str__(self):
		return str(self.id)




