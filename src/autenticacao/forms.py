from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):

    username = forms.CharField(
        label  = '',
        widget = forms.TextInput(attrs={'placeholder': 'Usuario', 'autofocus':'autofocus', 'class':'form-control digitl1'})
    )
    password = forms.CharField(
        label  = '',
        max_length = 8,
        widget = forms.PasswordInput(attrs={'placeholder': 'Senha' , 'class':'form-control digit18'})
    )

    error_messages = {
        'invalid_login': _("Por favor, entre com um usuario e senha valido. Note que ambos os campos diferenciam maiúsculas e minúsculas."),
        'inactive': _("Essa conta está inativa."),
        }


    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                            password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

        error_messages = {
            'invalid_login': _("Por favor, entre com um cpf e data de nascimento corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas."),
            'inactive': _("Essa conta está inativa."),
        }


    def confirm_login_allowed(self, user):
        """
        Controla se o Usuário pode fazer login. Essa é uma configuração de política. Independente da autenticação do usuário final. Esse comportamento padrão é para permitir login por usuários ativos e rejeitar login por usuários inativos.

        Se o utilizador não conseguir iniciar sessão, este método deverá
        `` Forms.ValidationError``.

        Se o usuário determinado pode efetuar logon, esse método deve retornar None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
