from django.forms import *

from app_syfy.models.genero import Genero


class GeneroForm(ModelForm):
    class Meta:
        model = Genero