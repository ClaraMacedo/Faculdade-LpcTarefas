from django.http import HttpResponse
from .models import  *

def index(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/usuario'>Usuarios</a></li>
                    <li><a href='/projeto'>Projetos</a></li>
                    <li><a href='/tarefa'>Tarefas</a></li>
                </ul>
            """
    return HttpResponse(html)
def listaUsuarios(request):
    html = "<h1>Lista de Usuarios</h1>"
    lista = Usuarios.objects.all()
    for i in lista:
        html += '<li><strong>{}</strong></li>'.format(i.nome)
    return HttpResponse(html)

def usuarioid(request, id):
    usuario= Usuario.objects.get(pk=id)
    return HttpResponse("<h2> Informações Usuario #" + "</h2>" + "<strong>Nome:</strong> " + str(usuario.nome)  + "<br>")
