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
        #criar registros no banco temporario
        classificacao = Classificacao(classificacao=18)
        classificacao.save()

        self.genero = Genero(nome='syfy')
        self.genero.save()

        self.genero1 = Genero(nome='syfy1')
        self.genero1.save()


        self.video = Video(
            titulo='DC-flash',duracao='10:00', classificacao=classificacao
        )
        self.video1 = Video(
            titulo='DC-flash1', duracao='10:00', classificacao=classificacao
        )
        self.video.save()
        self.video.genero.add(self.genero)
        self.video.save()

        self.video1.save()
        self.video1.genero.add(self.genero1)
        self.video1.save()

        self.client = Client()

    def status_url(self,url,pk):
        response = self.client.get(reverse(url, kwargs={'pk': pk}))
        return response.status_code

    def contains_video(self,video,genero):

        response=self.client.get(reverse('video-genero-list', kwargs={'pk': genero}))
        object_list=response.context[-1]['object_list']
        return video in object_list

    def not_contains_video(self,video,genero):
        response=self.client.get(reverse('video-genero-list', kwargs={'pk': genero}))
        object_list=response.context[-1]['object_list']
        return not video in object_list

    def count_list_video(self):
        response = self.client.get(reverse('video-list'))
        object_list = response.context[-1]['object_list']
        return len(object_list)

    def testObjectCreate(self):
        #testar a quantidade de obejetos criados
        self.assertEquals(Video.objects.count(), 2)

        #testar a listagem dos videos por categoria
        self.assertEquals(self.contains_video(self.video,self.genero.id),True)
        self.assertEquals(self.contains_video(self.video1,self.genero1.id),True)

        #testar erro da listagem dos videos por categoria
        self.assertEquals(self.not_contains_video(self.video, self.genero1.id), True)
        self.assertEquals(self.not_contains_video(self.video1, self.genero.id), True)

        #testar a quantagem de videos pela views
        self.assertEquals(self.count_list_video(), 2)

        #teste da url individual do primeiro video
        self.assertEquals(self.status_url('video-detail',1), 200)
