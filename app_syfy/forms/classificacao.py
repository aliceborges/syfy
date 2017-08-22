from django.forms import *

from app_syfy.models.classificacao import Classificacao


class ClassificacaoForm(ModelForm):
    class Meta:
        model = Classificacao