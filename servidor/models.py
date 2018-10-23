# -*- coding: UTF-8 -*-

from django.db import models

class Servidor(models.Model):
    registro = models.CharField(max_length=20)
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nome

class Cargo(models.Model):
    from parametros.models import Escolaridade
    from parametros.models import NaturezaDoCargo
    registro = models.IntegerField()
    denominacao = models.CharField(max_length=200)
    codigoCargo = models.CharField(verbose_name="Código do Cargo", max_length=20)
    simboloDeVencimento = models.CharField(verbose_name="Simbolo de Vencimento",max_length=20)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.SET_NULL,null=True)
    recrutamento = models.CharField(max_length=100)
    naurezaDoCargo = models.ForeignKey(NaturezaDoCargo,on_delete=models.SET_NULL,null=True)
    leiDeCriacao = models.CharField(verbose_name="Lei de Criação",max_length=100)
    poderDeLotacao = models.CharField(max_length=200,verbose_name="Poder de lotação")
    def __unicode__(self):
        return self.denominacao

class PerfisDeDiaria(models.Model):
    from parametros.models import Escolaridade
    registro = models.IntegerField(verbose_name='Registro N')
    tabela = models.CharField(max_length=100)
    dataDaTabela = models.DateField(verbose_name="Data da Tabela",auto_now=True)
    cargo = models.CharField(max_length=100)
    escolaridade = models.ForeignKey(Escolaridade,on_delete=models.SET_NULL,null=True)
    def __unicode__(self):
        return self.denominacao
##    categoriadeviagem = models.

class PortariasAutorizativa(models.Model):
    from parametros.models import DestinoDeViagens
    from parametros.models import OrigensDeViagens
    registro = models.IntegerField(primary_key=True,serialize=True,verbose_name="Registro N")
    portaria = models.CharField(max_length=10)
    dataExpedicao = models.DateField(verbose_name="Data da Expedição",auto_now_add=True)
    orgaoEmissor = models.CharField(max_length=100)
    nomeServidorEmissor = models.ForeignKey(Servidor,verbose_name="Nome do Servidor Emissor",on_delete=models.SET_NULL,null=True)
    cargoDoEmissor = models.ForeignKey(Cargo,on_delete=models.SET_NULL,null=True)
##    NomeServidorAutorizatario = models.ForeignKey(Servidor)
##    CargoDoServidorAutorizatario = models.ForeignKey(Cargo)
    destino = models.ForeignKey(DestinoDeViagens,on_delete=models.SET_NULL,null=True)
    orgao = models.ForeignKey(OrigensDeViagens,on_delete=models.SET_NULL,null=True)
    dataDoInicioDaViagem = models.DateField(verbose_name="Data do Início da Viagem")
    horaDoInicioDaViagem = models.TimeField(verbose_name="Hora do Início da Viagem")
    dataDoTerminioDaViagem = models.DateField(verbose_name="Data do Términio da viagem")
    horaDoTerminioDaViagem = models.TimeField(verbose_name="Hora do Términio da Viagem")
    missao = models.TextField(verbose_name="Missão")
    def __unicode__(self):
        return self.portaria

class UnidadesAdministrativa(models.Model):
    from endereco.models import Estado
    registro = models.AutoField(primary_key=True,serialize=True)
    siglaUnidadeAdministrativa = models.CharField(max_length=10,verbose_name='Sigla da Unidade Administrativa')
    unidadeAdministrativa = models.TextField(max_length=100,verbose_name="Unidade Administrativa")
    endereco = models.CharField(max_length=50,verbose_name="Endereço")
    numero = models.CharField(max_length=15)
    bairro = models.CharField(max_length=70)
    telefone = models.CharField(max_length=16)
    fax = models.CharField(max_length=16)
    email = models.EmailField()
    expedienteChegada = models.TimeField(verbose_name="Das")
    expedienteSaidaAlmoco = models.TimeField(verbose_name="às")
    expedienteEntradaAlmoco = models.TimeField(verbose_name="Das")
    expedienteSaida = models.TimeField(verbose_name="às")
    cep = models.CharField(verbose_name="Cep",max_length=15)
    municipios = models.CharField(verbose_name="Município",max_length=70)
    uf = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)
    class Meta:
        get_latest_by="siglaUnidadeAdministrativa"
    def __unicode__(self):
        return self.siglaUnidadeAdministrativa

