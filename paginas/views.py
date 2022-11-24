
from django.views.generic import TemplateView


# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'paginas/modelo.html'

class DemissoesView(TemplateView):
    template_name = 'paginas/demissoes.html'

class FeriasView(TemplateView):
    template_name = 'paginas/ferias.html'

class AfastamentosView(TemplateView):
    template_name = 'paginas/afastamentos.html'

class LicencasView(TemplateView):
    template_name = 'paginas/licencas.html'    