from django.shortcuts import render, reverse
from django.views.generic import CreateView, DeleteView,UpdateView
from django.contrib.auth import update_session_auth_hash,authenticate
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout


from cadastro.forms import UsuarioCreateForm
from cadastro.models.cadastro import User

class UsuarioCreateView(CreateView):
    """
    Para cadastro de novos usuários
    """
    form_class = UsuarioCreateForm
    success_url = reverse_lazy('home')
    template_name = 'cadastro/cadastro.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        self.object = form.save()

        #Hash senha
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        #Autentica usuario criado
        user = authenticate(username=username,
                            password=password)
        auth_login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())
