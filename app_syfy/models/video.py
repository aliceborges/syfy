# -*- coding: utf-8 -*-
from django.db import models
from app_syfy.models.ator import Ator
from app_syfy.models.genero import Genero
from app_syfy.models.classificacao import Classificacao
from django.urls import reverse
class Video(models.Model):
    titulo = models.CharField(max_length=250, help_text='Deve conter no máximo 250 caracteres.')
    descricao = models.CharField(max_length=500, help_text='Deve conter no máximo 250 caracteres.')
    elenco = models.ManyToManyField(Ator, help_text='Deve conter o elenco do filme',related_name="elenco")
    diretor = models.ManyToManyField(Ator, help_text='Deve conter o diretor.',related_name="diretor")
    genero = models.ManyToManyField(Genero, help_text='Deve conter o genero.',related_name="genero")
    classificacao = models.ForeignKey(Classificacao, help_text='Deve conter a classificacao indicativa do filme.',related_name="classificacao_indicativa")
    arquivo = models.FileField(help_text='Deve conter o arquivo de vídeo.',upload_to="upload/video" )
    youtube = models.URLField(max_length=200,help_text='Deve conter o arquivo de vídeo.' )
    imagem = models.ImageField(help_text='Deve conter a imagem do vídeo',upload_to="upload/imagem")
    duracao = models.TimeField()

    def __unicode__(self):
        return self.titulo

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})