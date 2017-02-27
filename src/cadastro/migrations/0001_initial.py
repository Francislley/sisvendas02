# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 01:26
from __future__ import unicode_literals

import cadastro.models.manager
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(error_messages={'unique': 'E-mail já registrado.'}, max_length=254, unique=True, verbose_name='E-mail')),
                ('username', models.CharField(error_messages={'unique': 'Usuario já registrado.'}, max_length=150, unique=True, verbose_name='Nome de Usuario')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w\\s]+$', 32), 'Use apenas letras e números para o nome.', 'invalid')], verbose_name='Nome')),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w\\s]+$', 32), 'Use apenas letras e números para o sobrenome.', 'invalid')], verbose_name='Sobrenome')),
                ('password', models.CharField(max_length=128, verbose_name='Senha')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Data da Atualização')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Registro')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrador')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
                'verbose_name': 'auth_user',
            },
            managers=[
                ('objects', cadastro.models.manager.UserManager()),
            ],
        ),
    ]