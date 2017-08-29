from django.forms import *

from app_syfy.models.ator import Ator


class AtorForm(ModelForm):
    class Meta:
        model = Ator
        fields = "__all__"