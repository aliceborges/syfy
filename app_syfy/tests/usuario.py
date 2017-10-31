# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase
from django.test import Client
from app_syfy.models import Usuario


class UsuarioTests(TestCase):
    def setUp(self):
        # create permissions group
        group_name = "administrador"
        self.group = Group(name=group_name)
        self.group.save()
        self.client = Client()

    # Alice esse ususario_add é sem executar o post com a view de criação - precisei criar por conta do teste de detalhes
    def usuario_add(self, first_name='Maria', last_name='da Silva', username='mariadasilva@gmail.com',
                    password='admin123', is_superuser=False, is_staff=False, is_active=True, grupo=None):
        usuario = Usuario.objects.create(first_name=first_name, last_name=last_name, username=username,
                                         password=password, is_superuser=is_superuser, is_staff=is_staff,
                                         is_active=is_active)
        if grupo != None:
            usuario.groups.add(grupo)
            usuario.save()
        return usuario

    def usuario_detail(self, usuario):
        response = self.client.get(reverse('usuario-detail', kwargs={'pk': usuario.id}))
        self.assertEqual(response.status_code, 200)

    def usuario_instance(self, usuario):
        # verifica se a classe instanciada foi realmente de Usuario
        self.assertTrue(isinstance(usuario, Usuario))

    def usuario_info(self, usuario):
        # verifica se retorna o useraname
        self.assertEqual(usuario.__unicode__(), usuario.username)

    def test_usuario(self):
        usuario1 = self.usuario_add()
        self.usuario_detail(usuario1)
        self.usuario_instance(usuario1)
        self.usuario_info(usuario1)

        usuario2 = self.usuario_add('João', 'da Silva', 'joaodasilva@gmail.com', 'admin123', False, False, True,
                                    self.group)
        self.usuario_detail(usuario2)
        self.usuario_instance(usuario2)
        self.usuario_info(usuario2)

        usuario3 = self.usuario_add('Marta', 'da Silva', 'martadasilva@gmail.com', 'admin123', True, False, True,
                                    self.group)
        self.usuario_detail(usuario3)
        self.usuario_instance(usuario3)
        self.usuario_info(usuario3)

        usuario4 = self.usuario_add('Admin', 'Admin', 'admin', 'admin123', True, True, True, self.group)
        self.usuario_detail(usuario4)
        self.usuario_instance(usuario4)
        self.usuario_info(usuario4)
