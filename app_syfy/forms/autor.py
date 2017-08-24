from django.forms import *

from app_syfy.models.ator import Autor


class AutorForm(ModelForm):
    class Meta:
        model = Autor