# -*- coding: UTF-8 -*-
from django.db import models
# Create your models here.

class Pais (models.Model):
    nome = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Paises"

class Estado (models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais,on_delete=models.SET_NULL,null=True)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Municipio (models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Bairro (models.Model):
    nome = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Endereco (models.Model):
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairro,on_delete=models.SET_NULL,null=True)
    municipio = models.ForeignKey(Municipio,on_delete=models.SET_NULL,null=True)
    def __unicode__(self):
        return self.cep+"/"+self.rua
    def __str__(self):
        return self.cep+"/"+self.rua

class Localidade (models.Model):
    nome = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome


