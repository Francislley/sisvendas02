from django.conf.urls import url
from cadastro.views import UsuarioCreateView

urlpatterns = [

    url(r'^$',UsuarioCreateView.as_view(), name='cadastro' ),
]
