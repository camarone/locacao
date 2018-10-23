# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

class Sdv(models.Model):
    from servidor.models import UnidadesAdministrativa
    from servidor.models import Servidor
    from servidor.models import Cargo
    from endereco.models import Localidade
    from parametros.models import TiposDeDespesasEmViagens

##    from parametros.models import Despesas
##    from parametros.models import StatusPC
    #~ from diarias.parametros.models import
    exercicio = models.CharField(max_length=4,default='2011')
    dataSolicitacao = models.DateField(verbose_name='Data Solicitação')
    unidade = models.ForeignKey(UnidadesAdministrativa,verbose_name='Unidade Administrativa',on_delete=models.SET_NULL,null=True)
    solicitante = models.ForeignKey(Servidor,on_delete=models.SET_NULL,null=True)
    cargo = models.ForeignKey(Cargo,on_delete=models.SET_NULL,null=True)
    periodoInicio = models.DateTimeField(verbose_name='Início')
    periodoTermino = models.DateTimeField(verbose_name='Término')
    localidade = models.ForeignKey(Localidade,on_delete=models.SET_NULL,null=True)
    diariaValorSolicitado = models.PositiveIntegerField(verbose_name='Diária Valor Solicitado')
    diariaValorAprovado = models.PositiveIntegerField(verbose_name='Diária Valor Aprovado')
    alimentacaoValorSolicitado = models.PositiveIntegerField(verbose_name='Alimentação Valor Solicitado')
    alimentacaoValorAprovado = models.PositiveIntegerField(verbose_name='Alimentacao Valor Aprovado')
    transporteValorSolicitado = models.PositiveIntegerField(verbose_name='Transporte Urbano Valor Solicitado')
    transporteValorAprovado = models.PositiveIntegerField(verbose_name='Transporte Valor Aprovado')
    passagemValorSolicitado = models.PositiveIntegerField(verbose_name='Passagem Valor Solicitado')
    passagemValorAprovado = models.PositiveIntegerField(verbose_name='Passagem Valor Aprovado')
    observacoes = models.TextField(verbose_name='Observação')
##    status = models.ForeignKey(StatusPC,on_delete=models.SET_NULL,null=True)


    def __unicode__(self):
        return u"%s" % self.name

    def related_label(self):
        return u"%s (%s)" % (self.name, self.id)

    def related_autocomplete_lookup(self):
        return u"%s,%s,%s" % (self.id, self.name, self.category)

    class Meta:
        verbose_name_plural = "Solicitações"

    def __unicode__(self):
        return self.solicitante.nome

class Rcv(models.Model):
	from servidor.models import UnidadesAdministrativa
	from servidor.models import Servidor
	from servidor.models import Cargo
	from endereco.models import Localidade
	from parametros.models import TiposDeDespesasEmViagens
##	from parametros.models import Despesas
##	from parametros.models import StatusPC
	exercicio = models.CharField(max_length=4,default='2011')
	dataSolicitacao = models.DateField(verbose_name='Data Solicitação')
	unidade = models.ForeignKey(UnidadesAdministrativa,verbose_name='Unidade Administrativa',on_delete=models.SET_NULL,null=True)
	solicitante = models.ForeignKey(Servidor,on_delete=models.SET_NULL,null=True)
	cargo = models.ForeignKey(Cargo,on_delete=models.SET_NULL,null=True)
	periodoInicio = models.DateTimeField(verbose_name='Início')
	periodoTermino = models.DateTimeField(verbose_name='Término')
	objetivo = models.TextField(verbose_name='Objetivo da Viagem')
	atividades = models.TextField(verbose_name='Atividades Realizadas')
	justificativa = models.TextField(verbose_name='Justificativa')

class QualificaRquisicao(models.Model):
    from servidor.models import PortariasAutorizativa
    portariaautprizativa = models.ForeignKey(PortariasAutorizativa,on_delete=models.SET_NULL,null=True)
    dataPortaria = models.DateField(verbose_name="Data da Portaria")
    cargodoservidor = models.CharField(verbose_name="Cargo do Servidor",max_length=100)
    unidade = models.CharField(max_length=100,verbose_name="Unidades")
    exercicio = models.CharField(max_length=100,verbose_name="exercicio")
    #~ dataPortaria = unidade = models.DateTimeField(verbose_name="Data/Hora")
