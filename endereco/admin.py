from endereco.models import Endereco

from endereco.models import Estado
from endereco.models import Pais
from endereco.models import Municipio
from endereco.models import Bairro
from endereco.models import Localidade

from django.contrib import admin



admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Localidade)