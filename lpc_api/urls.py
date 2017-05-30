"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from tastypie.api import Api
from django.contrib import admin
from tarefa.api.resources import UsuarioResource, ProjetoResource, TarefaResource, ProjetoUsuarioResource

from tarefa.views import *

v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(ProjetoResource())
v1_api.register(TarefaResource())
v1_api.register(ProjetoUsuarioResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^usuario/', listaUsuarios, name='listaUsuarios'),
    #url(r'^usuario/([0-9]{1})', usuarioId, name='usuarioId'),
    #url(r'^projeto/', listaProjetos, name='listaProjetos'),
    #url(r'^projeto/([0-9]{1})', projetoId, name='projetoId'),
    #url(r'^tarefa/', listaTarefas, name='listaTarefas'),
    #url(r'^tarefa/([0-9]{1})', tarefaId, name='tarefaId'),
    #url(r'^projetousuario/', listaProjetousuarios, name='listaProjetousuarios'),
    #url(r'^projetousuario/([0-9]{1})', projetousuarioId, name='projetousuarioId'),
    url(r'^api/', include(v1_api.urls)),

]
