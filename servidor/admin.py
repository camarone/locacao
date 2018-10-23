from servidor.models import Servidor
from servidor.models import Cargo
from servidor.models import PerfisDeDiaria
from servidor.models import PortariasAutorizativa
from servidor.models import UnidadesAdministrativa


from django.contrib import admin

admin.site.register(Servidor)
admin.site.register(Cargo)
admin.site.register(PerfisDeDiaria)
admin.site.register(PortariasAutorizativa)

##class UnidadesAdministrativa(admin.TabularInline)

class UnidadesAdministrativaAdmin(admin.ModelAdmin):
    search_fields = ('siglaUnidadeAdministrativa',)
    fieldsets = [
    (None,                  {'fields':['siglaUnidadeAdministrativa','unidadeAdministrativa']}),
    ('Expediente',    {'fields':['expedienteChegada','expedienteSaidaAlmoco','expedienteEntradaAlmoco','expedienteSaida']}),
    ]
    list_display = ('siglaUnidadeAdministrativa','unidadeAdministrativa')
    list_filter = ['email']

admin.site.register(UnidadesAdministrativa,UnidadesAdministrativaAdmin)