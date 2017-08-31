from django.forms import *

from django.contrib.auth.models import User
from app_syfy.models.usuario import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        #fields = "__all__"
        exclude =('favorito',)