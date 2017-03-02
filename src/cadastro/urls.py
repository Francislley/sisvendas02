from django.conf.urls import url
from cadastro import views

urlpatterns = [

    url(r'^$',views.UsuarioCreateView.as_view(), name='cadastro' ),
]
