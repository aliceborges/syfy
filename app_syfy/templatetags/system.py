from django import template

from app_syfy.models import Genero

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()



@register.simple_tag
def generos():
    generos = Genero.objects.all()
    if generos:
        return generos
    return None
