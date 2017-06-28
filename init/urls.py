from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
url(r'^$', auth_views.login, {'template_name':'login.html'}, name='login'),
url(r'^cerrar/$', auth_views.logout_then_login,    name='logout'),
url(r'^index/$', views.index, name='index'),
]