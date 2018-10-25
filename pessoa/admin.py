from django.contrib import admin

from .models import Pessoa
from .models import CadastroDeAluguel
from django.http import HttpResponseRedirect
from django.utils.html import format_html, format_html_join, mark_safe
from django.utils.translation import gettext_lazy as _
admin.site.register(Pessoa)


class CadastroDeAluguelAdmin(admin.ModelAdmin):

    #autocomplete_fields = ['usuario', 'comodante']
    list_display = ('usuario', 'comodante', 'cadeira', 'termo_de_Concessao')

    list_filter = ['dataRequerimento', ]
    ordering = ['usuario']
    date_hierarchy = 'dataRequerimento'
    actions_selection_counter = False
    actions_on_top = False
    actions_on_bottom = True



    def termo_de_Concessao(self, obj):
        def __str__(self):
            return 'Termo de Concessão'

        def __unicode__(self):
            return 'Termo de Concessão'

        return format_html(
            '<a href="http://127.0.0.1:8000/pessoa/gerarcontrato/%s/">Contrato</a><a '
             % (
            obj.id))

    termo_de_Concessao.short_description = 'Termo de Concessão'


    #search_fields = ['usuario__nome','comodante__nome']
    #prepopulated_fields = {"mae": ("quadra","lote")}

    fieldsets = [
        ('Cadastro de Locação de Cadeira', {
            'classes': ('wide ', 'extrapretty'),
            'description': (
                'Cadastro de locação de cadeiras com usuario e requerente. Não esquecer de fazer o cadastro completo do '
                'Requerente para emitir a guia de Autorização'),
            'fields': [ ('usuario', 'parentesco'),('dataRequerimento', 'dataLocacao'),
                       ]}),
    ]
admin.site.register(CadastroDeAluguel,CadastroDeAluguelAdmin)