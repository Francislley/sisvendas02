from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from datetime import datetime
from django.core.mail import send_mail

from cadastro.models.manager import UserManager

import re

class User(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(
        primary_key=True
    )

    email = models.EmailField(
            verbose_name=_(u'E-mail'),
            max_length=254,
            unique=True,
            null=False,
            blank=False,
            error_messages={
            'unique': _(u"E-mail já registrado."),
        },
    )

    username = models.CharField(
            verbose_name=_(u'Nome de Usuario'),
            max_length=150,
            unique=True,
            null=False,
            blank=False,
            error_messages={
            'unique': _(u"Usuario já registrado."),
        },
    )

    first_name = models.CharField(
            verbose_name=_(u'Nome'),
            max_length=30,
            null=False,
            blank=False,
            validators=[
                validators.RegexValidator
                    (re.compile('^[\w\s]+$'),
                    _('Use apenas letras e números para o nome.'),
                    _('invalid'))]
    )

    last_name = models.CharField(
            verbose_name=_(u'Sobrenome'),
            max_length=30,
            null=False,
            blank=False,
            validators=[
                validators.RegexValidator
                    (re.compile('^[\w\s]+$'),
                    _('Use apenas letras e números para o sobrenome.'),
                    _('invalid'))]
    )

    password = models.CharField(
            verbose_name=_(u'Senha'),
            max_length=128,
            null=False,
            blank=False,
        )

    date_update = models.DateTimeField(
            verbose_name=_(u'Data da Atualização'),
            auto_now=True,
    )

    date_joined = models.DateTimeField(
            verbose_name=_(u'Data de Registro'),
            auto_now_add=True,
    )

    is_active = models.BooleanField(
            verbose_name=_(u'Ativo'),
            default=True,
    )
    is_superuser = models.BooleanField(
            verbose_name=_(u'Administrador'),
            default=False
    )
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']


    class Meta:
        db_table = 'auth_user'
        verbose_name = _('auth_user')

    def get_full_name(self):
        '''
        Retorna o primeiro e segundo nome com espaço entre eles
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return self.full_name.strip()

    def get_short_name(self):
        '''
        Retorna só o primeiro nome
        '''
        return self.first_name
