from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^crear_consumo/$', views.crear_consumo, name='crear_consumo'),
    url(r'^compra_materiales/$', views.compra_materiales, name='compra_materiales'),
    url(r'^Anticipos_Regado/$', views.Anticipos_Regado, name='Anticipos_Regado'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^Operacion/$', views.Operacion, name='Operacion'),
    url(r'^Gastos_Varios/$', views.Gastos_Varios, name='Gastos_Varios'),
    url(r'^Despacho/$', views.Despacho, name='Despacho'),
    url(r'^Viajes_internos/$', views.Viajes_internos, name='Viajes_internos'),
    url(r'^', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^cerrar/$', auth_views.logout_then_login, name='logout'),
    url(r'^index/$', views.index, name='index'),
     url(r'^admin/', admin.site.urls),

]
