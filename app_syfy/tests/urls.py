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

        self.client = Client()


    def status_url(self,url):
        response = self.client.get(reverse(url))
        return response.status_code

    # def status_url_absolute(self, url):
    #     response = self.client.get(url)
    #     return response.status_code


    def testObjectCreate(self):
        self.assertEquals(self.status_url('home'), 200)
