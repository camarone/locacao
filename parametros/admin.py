from parametros.models import EstadoCivil
from parametros.models import Nacionalidade
from parametros.models import UnidadeDeMedida
from parametros.models import CategoriaDestinoViagem
from parametros.models import SiglaDaParcelaDeDiaria
from parametros.models import NivelDaDiaria
from parametros.models import Escolaridade
from parametros.models import NaturezaDoCargo
from parametros.models import OrigensDeViagens
from parametros.models import TiposDeDespesasEmViagens
from parametros.models import TipoDeTransporte
from parametros.models import DestinoDeViagens

from django.contrib import admin

admin.site.register(TipoDeTransporte)
admin.site.register(TiposDeDespesasEmViagens)
admin.site.register(OrigensDeViagens)
admin.site.register(DestinoDeViagens)
admin.site.register(NaturezaDoCargo)
admin.site.register(Escolaridade)
admin.site.register(NivelDaDiaria)
admin.site.register(SiglaDaParcelaDeDiaria)
admin.site.register(CategoriaDestinoViagem)
admin.site.register(UnidadeDeMedida)
admin.site.register(EstadoCivil)
admin.site.register(Nacionalidade)

