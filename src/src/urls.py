from django.conf.urls import url,include
from django.conf import settings
from autenticacao.views import LoginView, LogoutView, home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^cadastro/', include('cadastro.urls', namespace='cadastro')),
]
