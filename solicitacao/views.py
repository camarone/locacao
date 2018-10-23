# Create your views here.
from diarias.solicitacao.models import Sdv
from django.http import HttpResponse
from autocomplete.views import AutocompleteView

autocomplete = AutocompleteView('solicitacao')
def index(request):
    latest_poll_list = Sdv.objects.all().order_by('exercicio')
    output = ', '.join([p.observacoes for p in latest_poll_list])
    return HttpResponse(output)
