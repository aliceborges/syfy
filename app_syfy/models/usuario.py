# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from app_syfy.models.video import Video
from django.urls import reverse

class Usuario(User):
    favorito = models.ManyToManyField(Video, help_text='Deve conter os favoritos do usuario.',related_name="favoritos")


    def __unicode__(self):
        return self.username

    class Meta:
        app_label = 'app_syfy'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def get_absolute_url(self):
        return reverse('usuario-detail', kwargs={'pk': self.pk})
