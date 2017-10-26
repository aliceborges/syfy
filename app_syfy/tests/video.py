# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_syfy.models import Video, Classificacao
from django.test import TestCase

# Create your tests here.
# from django.test import Client
# from django.core.urlresolvers import reverse
# client = Client()
# response = client.get(reverse('blog_index'))
from django.test import Client
from django.core.urlresolvers import reverse

class TesteVideo(TestCase):
    def setUp(self):
        self.classificacao = Classificacao(classificacao=18)
        self.classificacao.save()
        self.video = Video.objects.get_or_create(
            titulo='DC-flash',duracao='10:00', classificacao=self.classificacao
        )
        self.client = Client()


    # def status_url(self):
    #     response = self.client.get(reverse('home'))
    #     return response.status_code


    def testObjectCreate(self):
        self.assertEquals(Video.objects.count(), 1)
