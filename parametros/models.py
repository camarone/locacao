# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class EstadoCivil(models.Model):
    nome = models.CharField(max_length=100)
    def __unicode__ (self):
        return self.nome
    def __str__(self):
        return self.nome

class Nacionalidade(models.Model):
    nome = models.CharField(max_length=100)
    def __unicode__ (self):
        return self.nome
    def __str__(self):
        return self.nome

class UnidadeDeMedida(models.Model):
    nome = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class CategoriaDestinoViagem(models.Model):
    nome = models.CharField(verbose_name="Nome Categoria",max_length=100)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class SiglaDaParcelaDeDiaria(models.Model):
    sigla = models.CharField(max_length=20,verbose_name="Sigla da Parcela de Diária")
    status = models.BooleanField()
    descricao = models.TextField(verbose_name="Descrição da Parcela de Diária",max_length=300)
    def __unicode__(self):
        return '%s' % (self.sigla)
    def __str__(self):
        return '%s' % (self.sigla)


class NivelDaDiaria(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField()
    descricao = models.TextField(max_length=200)
    def __unicode__(self):
        return '%s' % (self.nome)
    def __str__(self):
        return '%s' % (self.nome)


class Escolaridade(models.Model):
    nome = models.CharField(max_length=70)
    descricao = models.TextField(max_length=200)
    def __unicode__(self):
        return '%s' % (self.nome)
    def __str__(self):
        return '%s' % (self.nome)


class NaturezaDoCargo(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField(max_length=200)
    def __unicode__(self):
        return '%s' % (self.nome)
    def __str__(self):
        return '%s' % (self.nome)



##class OrgaosDeOrigemDeViagens(models.Model):
##    nome = models.CharField(verbose_name="Órgãos de Origem de Viagens",max_length=50)
##    def __unicode__(self):
##        return self.nome
##
##class LocaisDeOrigemDeViagens(models.Model):
##    nome = models.CharField(verbose_name="Locais de Origem de Viagens",max_length=50)
##    def __unicode__(self):
##        return self.nome


class OrigensDeViagens(models.Model):
    codigo = models.AutoField(primary_key=True,serialize=True)
    locaisDeOrigemDeViagens = models.CharField(max_length=50)
    orgaosDeOrigemDeViagens = models.CharField(max_length=50)
##    locais = models.ForeignKey(LocaisDeOrigemDeViagens)
##    orgao = models.ForeignKey(OrgaosDeOrigemDeViagens)
    def __unicode__(self):
        return '%s/%s' % (self.locaisDeOrigemDeViagens,self.orgaosDeOrigemDeViagens)
    def __str__(self):
        return '%s/%s' % (self.locaisDeOrigemDeViagens,self.orgaosDeOrigemDeViagens)


class DestinoDeViagens(models.Model):
    registro = models.AutoField(verbose_name="Registro N",serialize=True,primary_key=True)
    locaisDeDestinoDeViagens = models.CharField(max_length=50,verbose_name="Locais de Destino de Viagens")
    orgaosDeDestinoDeViagens = models.CharField(max_length=50,verbose_name="Òrgãos de Destino de Viagens")
    FinalidadeDaViagem = models.CharField(max_length=50,verbose_name="Finalidade da Viagem")
    def __unicode__(self):
        return '%s/%s' % (self.registro,self.FinalidadeDaViagem)
    def __str__(self):
        return '%s/%s' % (self.registro,self.FinalidadeDaViagem)


class TiposDeDespesasEmViagens(models.Model):
    registro = models.IntegerField(verbose_name="Registro N",primary_key=True)
    descricao = models.CharField(verbose_name="Descrição da Dspesa",max_length=50)
    def __unicode__(self):
        return '%s/%s' % (self.registro,self.descricao)
    def __str__(self):
        return '%s/%s' % (self.registro,self.descricao)

class TipoDeTransporte(models.Model):
    registro = models.AutoField(primary_key=True,serialize=True)
    tipoDeTransport = models.TextField(verbose_name='Tipo de Transporte')
    natureza = models.CharField(max_length=50,verbose_name="Natureza da Propiedade do tipo de transporte")

    def __unicode__(self):
        return '%s/%s' % (self.nome,self.descricao)
    def __str__(self):
        return '%s/%s' % (self.nome,self.descricao)
# Create your models here.