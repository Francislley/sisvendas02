from django.conf.urls import url,include
from django.conf import settings

urlpatterns = [
    url(r'^cadastro/', include('cadastro.urls', namespace='cadastro')),
    url(r'^', include('autenticacao.urls', namespace='autenticacao')),

]
