from django.forms import *

from app_syfy.models.autor import Autor


class AutorForm(ModelForm):
    class Meta:
        model = Autor