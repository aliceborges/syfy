# -*- coding: utf-8 -*-
from django.db import models

class Classificacao(models.Model):
    classificacao = models.IntegerField(max_length=3, help_text='Deve conter no máximo 3 caracteres.')

    def __unicode__(self):
        return self.classificacao

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Classificacao'
        verbose_name_plural = 'Classificacoes'