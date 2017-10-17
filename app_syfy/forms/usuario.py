from django.forms import *

from django.contrib.auth.models import User
from app_syfy.models.usuario import Usuario

class UsuarioForm(ModelForm):
    password = CharField(widget=PasswordInput())
    username = EmailField()
    class Meta:
        model = Usuario
        #fields = "__all__"
        exclude =('email','favorito', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined')
