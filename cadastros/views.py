from django.views.generic.edit import CreateView

from .models import Demissoe, Feria, Afastamento, Licenca

from django.urls import reverse_lazy

# Create your views here.

class DemissoeCreate(CreateView):
    model = Demissoe
    fields = ['num_registro', 'nome', 'sede_empresarial', 'setor']
    template_name = 'cadastros/form-demissoes.html'
    success_url = reverse_lazy('index')

class FeriaCreate(CreateView):
    model = Feria
    fields = ['num_registro', 'nome', 'sede_empresarial', 'setor']
    template_name = 'cadastros/form-ferias.html'
    success_url = reverse_lazy('index')

class AfastamentoCreate(CreateView):
    model = Afastamento
    fields = ['num_registro', 'nome', 'sede_empresarial', 'setor']
    template_name = 'cadastros/form-afastamentos.html'
    success_url = reverse_lazy('index')


class LicencaCreate(CreateView):
    model = Licenca
    fields = ['num_registro', 'nome', 'sede_empresarial', 'setor']
    template_name= 'cadastros/form-licencas.html'
    success_url = reverse_lazy('index')


