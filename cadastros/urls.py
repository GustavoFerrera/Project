from django.urls import path

#todas as vies que a gente criou
from .views import DemissoeCreate, FeriaCreate, AfastamentoCreate, LicencaCreate


urlpatterns = [
    path('portal/demissoes', DemissoeCreate.as_view(), name="portal-demissoes"),
    path('portal/ferias', FeriaCreate.as_view(), name="portal-ferias"),
    path('portal/afastamentos', AfastamentoCreate.as_view(), name="portal-afastamentos"),
    path('portal/licencas', LicencaCreate.as_view(), name="portal-licencas"),
]