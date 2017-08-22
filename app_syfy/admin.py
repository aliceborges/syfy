# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app_syfy.models.usuario import Usuario
from app_syfy.models.autor import Autor
from app_syfy.models.classificacao import Classificacao
from app_syfy.models.genero import Genero
from app_syfy.models.video import Video

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Video)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Classificacao)