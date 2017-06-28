from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils import timezone
from .forms import ConsumoForm, IngresoForm, CompramaterialesForm, OperacionForm, AnticiposRegadoForm, GastosVariosForm, DespachoForm, Viajes_internosForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required()
def crear_consumo(request):

    if request.method == "POST":
        form = ConsumoForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = ConsumoForm()
        return render(request, 'crear_consumo.html', {'form': form})


@login_required()
def ingresar(request):

    if request.method == "POST":
        form = IngresoForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = IngresoForm()
        return render(request, 'ingresar.html', {'form': form})

@login_required()
def compra_materiales(request):

    if request.method == "POST":
        form = CompramaterialesForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = CompramaterialesForm()
        return render(request, 'compra_materiales.html', {'form': form})

@login_required()
def Anticipos_Regado(request):

    if request.method == "POST":
        form = AnticiposRegadoForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = AnticiposRegadoForm()
        return render(request, 'Anticipos_Regado.html', {'form': form})

@login_required()
def Operacion(request):

    if request.method == "POST":
        form = OperacionForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = OperacionForm()
        return render(request, 'Operacion.html', {'form': form})

@login_required()
def Gastos_Varios(request):

    if request.method == "POST":
        form = GastosVariosForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = GastosVariosForm()
        return render(request, 'Gastos_Varios.html', {'form': form})

@login_required()
def Despacho(request):

    if request.method == "POST":
        form = DespachoForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = DespachoForm()
        return render(request, 'Despacho.html', {'form': form})

@login_required()
def Viajes_internos(request):

    if request.method == "POST":
        form = Viajes_internosForm(request.POST)
        
        if form.is_valid():
            message = form.save()
            message.timestamp = timezone.now()
            message.save()
            return HttpResponseRedirect('/home/')
    
    else:
        form = Viajes_internosForm()
        return render(request, 'Viajes_internos.html', {'form': form})

@login_required()
def home(request):
    return render(request, "home.html")