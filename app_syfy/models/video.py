# -*- coding: utf-8 -*-
from django.db import models
from app_syfy.models.autor import Autor
from app_syfy.models.genero import Genero
from app_syfy.models.classificacao import Classificacao

class Video(models.Model):
    titulo = models.CharField(max_length=250, help_text='Deve conter no máximo 250 caracteres.')
    descricao = models.CharField(max_length=500, help_text='Deve conter no máximo 250 caracteres.')
    elenco = models.ManyToManyField(Autor, help_text='Deve conter o elenco do filme',related_name="elenco")
    diretor = models.ManyToManyField(Autor, help_text='Deve conter o diretor.',related_name="diretor")
    genero = models.ManyToManyField(Genero, help_text='Deve conter o genero.',related_name="genero")
    classificacao = models.ManyToManyField(Classificacao, help_text='Deve conter a classificacao indicativa do filme.',related_name="classificacao_indicativa")

    def __unicode__(self):
        return self.titulo

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
