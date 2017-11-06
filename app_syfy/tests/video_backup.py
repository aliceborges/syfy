# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_syfy.models import Video, Classificacao, Genero
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
        classificacao = Classificacao(classificacao=18)
        classificacao.save()
        genero = Genero(nome='syfy')
        genero1=genero.save()
        classificacao.save()
        self.video = Video.objects.get_or_create(
            titulo='DC-flash',duracao='10:00', classificacao=classificacao
        )
        self.video = Video.objects.get_or_create(
            titulo='DC-flash',duracao='10:00', classificacao=classificacao
        )
        #self.video.save()
        # print(self.video[0].genero)
        # self.video[0].genero.add(genero)


        self.client = Client()


    # def status_url(self):
    #     response = self.client.get(reverse('home'))
    #     return response.status_code

    # def contains_video(self,video,genero):
    #     #response = self.client.get(url)
    #     response=self.client.get(reverse('video-list-genero'), {'pk': genero})
    #     object_list=response.context[-1]['object_list']
    #     print(object_list)
    #     self.assertContains(self.video,)


    def testObjectCreate(self):
        self.assertEquals(Video.objects.count(), 1)
