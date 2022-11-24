from django.urls import path

#todas as vies que a gente criou
from .views import PaginaInicial, DemissoesView, FeriasView, AfastamentosView, LicencasView
from cadastros.views import DemissoeCreate

urlpatterns = [
     # path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('', PaginaInicial.as_view(), name='index'),
    path('demissoes/', DemissoesView.as_view(), name='demissoes'),
    path('ferias/', FeriasView.as_view(), name='ferias'),
    path('afastamentos/', AfastamentosView.as_view(), name='afastamentos'),
    path('licencas/', LicencasView.as_view(), name='licencas'),
   path('teste/', DemissoeCreate.as_view(), name='teste'),
]