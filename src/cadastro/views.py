from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,UpdateView
from django.contrib.auth import update_session_auth_hash,authenticate


from cadastro.forms import UsuarioCreateForm

class UsuarioCreateView(CreateView):
    form_class = UsuarioCreateForm
    # success_url = reverse_lazy('')
    template_name = 'cadastro/cadastro.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        self.object = form.save()

        #Autentica usuario criado
        user = authenticate(username=username,
                            password=password)
        auth_login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())
