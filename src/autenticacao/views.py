from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import FormView,RedirectView,TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator


from autenticacao.forms import LoginForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')


    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """
        Define um cookie de teste para garantir que o usuário
        tenha cookies ativados
        """
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # Se o cookie de teste funcionou, vá em frente e
        # Apagá-lo já que não é mais necessário
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    Fornece aos usuários a capacidade de efetuar logout
    """
    url = '../'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

def home(request):
    template_name = 'home.html'

    return render(request, template_name)
