from django.conf.urls import url
from cadastro.views import UsuarioCreateView

urlpatterns = [

    url(r'^$',UsuarioCreateView.as_view(), name='cadastro' ),
    url(r'edicao/^$',UsuarioCreateView.as_view(), name='edicao' ),
]
