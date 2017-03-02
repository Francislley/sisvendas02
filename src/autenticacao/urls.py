from django.conf.urls import url
from autenticacao import views


urlpatterns = [
    url(r'^$',login.as_view(), name='login' ),

]
