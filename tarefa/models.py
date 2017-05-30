from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)
    senha = models.CharField('email', max_length=200)


    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)


class Projeto(models.Model):
    nome = models.CharField('issn', max_length=200)
    
    def __str__(self):
        return '{}'.format(self.issn)


class Tarefa(models.Model):
    nome = models.CharField('nome', max_length=200)
    dataEHoraDaInscricao = models.DateTimeField('dataEHoraDaInscricao', default=timezone.now)
    usuario= models.ForeignKey('Usuario')
    projeto= models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.nome)

class ProjetoUsuario(models.Model):
    projeto = models.ForeignKey('Projeto')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.artigoCientifico)
