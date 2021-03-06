# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

class Ator(models.Model):
    nome = models.CharField(max_length=250, help_text='Deve conter no máximo 250 caracteres.')

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('autor-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
