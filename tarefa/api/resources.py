from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from tarefa.models import Usuario, Projeto, Tarefa, ProjetoUsuario
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']

class UsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não pode-se apagar lista completa!')
    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        resource_name = 'usuario'
        filtering = {
            "nome": ('exact', 'startswith',)
        }

class ProjetoResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não pode-se apagar lista completa!')
    class Meta:
        queryset = Projeto.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
            }

class TarefaResource(ModelResource):
    usuario= fields.ToOneField(UsuarioResource, 'usuario')
    projeto= fields.ToOneField(ProjetoResource, 'projeto')
    def obj_create(self, bundle, **kwargs):
        projeto=bundle.data['projeto'].split('/')
        if not(Tarefa.objects.filter(nome=bundle.data['nome'].upper())):
            print("\nTarefa não tem nehum projeto\n")
            tarefa=Tarefa()
            tarefa.descricao= bundle.data['nome'].upper()
            tarefa.save()
            bundle.obj= tarefa
            return bundle
        else:
            raise Unauthorized('Esta tarefa já foi cadastrada')

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não pode-se apagar lista completa!')

    def delete(self, bundle, **kwargs):
        usuarioPK= bundle.data['Usuario'].split('/')

        if(Tarefa.objects.filter(usuario=usuarioPK[4])):
            tarefa=Tarefa()
            tarefa.delete()
        else:
            raise Unauthorized('Este usuário não esta autorrizado a apagar esta tarefa')

    class Meta:
        queryset = Tarefa.objects.all()
        allowed_methods = ['get','post','delete','put']
        resource_name = 'tarefa'
        authorization=Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }


class ProjetoUsuarioResource(ModelResource):
    usuario= fields.ToOneField(UsuarioResource, 'usuario')
    projeto= fields.ToOneField(ProjetoResource, 'projeto')
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não pode-se apagar lista completa!')

    class Meta:
        queryset = ProjetoUsuario.objects.all()
        allowed_methods = ['get','post','delete','put']
        resource_name = 'projetousuario'
        authorization=Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }
