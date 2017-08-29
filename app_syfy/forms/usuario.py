from django.forms import *

from django.contrib.auth.models import User


class AutorForm(ModelForm):
    class Meta:
        model = User