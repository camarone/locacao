# -*- coding: UTF-8 -*-
from solicitacao.models import Sdv
from solicitacao.models import Rcv
from django.contrib import admin
from servidor.models import Servidor
from django import template
from django.shortcuts import render_to_response

class SdvAdmin(admin.ModelAdmin):
    pass
##	fieldsets = [
##	(None,                  {'fields':[('exercicio','dataSolicitacao'),('unidade','solicitante'),('cargo','localidade'),]}),
##	('Périodo previsto para a viagem', {'fields':[('periodoInicio','periodoTermino')]}),
##	('Despesas',        {'fields':[('diariaValorSolicitado','diariaValorAprovado'),('alimentacaoValorSolicitado','alimentacaoValorAprovado'),('transporteValorSolicitado','transporteValorAprovado'),('passagemValorSolicitado','passagemValorAprovado')]}),
##	(None,{'fields':['observacoes','status']})
##	]
##	list_display = ('solicitante','dataSolicitacao','localidade')
##	list_filter = ['exercicio','dataSolicitacao','status']


admin.site.register(Sdv, SdvAdmin)

class RcvAdmin(admin.ModelAdmin):
	 pass

admin.site.register(Rcv, SdvAdmin)

#~ class SdvAdmin(admin.ModelAdmin):


    #~ search_fields = ('^solicitante',)
    #~ fieldsets = [
    #~ (None,                  {'fields':[('exercicio','dataSolicitacao'),('unidade','solicitante'),('cargo','localidade'),]}),
    #~ ('Périodo previsto para a viagem', {'fields':[('periodoInicio','periodoTermino')]}),
    #~ ('Despesas',        {'fields':[('diariaValorSolicitado','diariaValorAprovado'),('alimentacaoValorSolicitado','alimentacaoValorAprovado'),('transporteValorSolicitado','transporteValorAprovado'),('passagemValorSolicitado','passagemValorAprovado')]}),
    #~ (None,{'fields':['observacoes','status']})
     #~ ]
    #~ list_display = ('solicitante','dataSolicitacao','localidade')
    #~ list_filter = ['exercicio','dataSolicitacao','status']
    #~ autocomplete_lookup_fields = {'fk': ['solicitante'],}
    #~ raw_id_fields = ('solicitante',)

#~ admin.site.register(Sdv,SdvAdmin)



