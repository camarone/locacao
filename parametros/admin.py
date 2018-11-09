from django.contrib import admin

from .models import  Estado, Cidade, Bairro, Profissao, Nacionalidade, Avaliador, Cadeira, Parentesco, Estadocivil, Rotariano


class EstadoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class CidadeAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class BairroAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class ProfissaoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class NacionalidadeAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class AvaliadorAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class CadeiraAdmin(admin.ModelAdmin):
    ordering = ['numero']
    search_fields = ['numero']

class ParentescoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']
class EstadocivilAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

class RotarianoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']

admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)
admin.site.register(Bairro,BairroAdmin)
admin.site.register(Profissao,ProfissaoAdmin)
admin.site.register(Nacionalidade,NacionalidadeAdmin)
admin.site.register(Avaliador,AvaliadorAdmin)
admin.site.register(Cadeira,CadeiraAdmin)
admin.site.register(Parentesco,ParentescoAdmin)
admin.site.register(Estadocivil,EstadocivilAdmin)
admin.site.register(Rotariano,RotarianoAdmin)
