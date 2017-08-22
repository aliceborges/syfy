# -*- coding: utf-8 -*-
from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=250, help_text='Deve conter no máximo 250 caracteres.')

    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
