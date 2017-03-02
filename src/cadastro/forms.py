from django import forms
from django.utils.translation import ugettext_lazy as _

from cadastro.models.cadastro import User

class UsuarioCreateForm(forms.ModelForm):

    password2 = forms.CharField(
        label = u'Confirmar a senha',
        max_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar a senha.'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

        labels = {
            'first_name':_(u'Nome'),
            'last_name':_(u'Sobrenome'),
            'email':_(u'E-Mail'),
            'username':_(u'Usuario'),
            'password':_(u'Senha'),
            }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Sobrenome'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'email@email.com'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Nome de Usuario'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Senha'}),
        }

        def clean_password2(self):
            # Verifique se as duas senhas estão iguais
            password = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("password2")
            if password and password2 and password != password2:
                raise forms.ValidationError("Senha incompativeis")
            return password2

        def save(self, commit=True):
            # Salva a senha fornecida em formato hash
            user = super(CadastroCreateForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user
