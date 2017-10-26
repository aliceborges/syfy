# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app_syfy.models import Video
from django.test import TestCase

# Create your tests here.
# from django.test import Client
# from django.core.urlresolvers import reverse
# client = Client()
# response = client.get(reverse('blog_index'))
from django.test import Client
from django.core.urlresolvers import reverse

class TesteHome(TestCase):
    def setUp(self):

        # self.video = Video.objects.get_or_create(
        #     titulo='DC-flash',duracao='10:00'
        # )
        self.client = Client()


    def status_url(self):
        response = self.client.get(reverse('home'))
        return response.status_code


    def testObjectCreate(self):
        self.assertEquals(self.status_url(), 200)
