from django.contrib import admin
from tarefa.models import Usuario, Projeto, Tarefa, ProjetoUsuario


admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(ProjetoUsuario)
