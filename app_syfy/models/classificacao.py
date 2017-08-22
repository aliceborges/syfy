# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

class Classificacao(models.Model):
    classificacao = models.IntegerField(max_length=3, help_text='Deve conter no máximo 3 caracteres.')

    def __unicode__(self):
        return self.classificacao

    def get_absolute_url(self):
        return reverse('classificacao-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Classificacao'
        verbose_name_plural = 'Classificacoes'