# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from app_syfy.models import *
import csv
#from django.
import hashlib

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "csv/genero.csv" na raiz do projeto.'
         
           ".'''


    def _create_genero(self):
        with open('csv/genero.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for i,row in enumerate(reader):
                # if not Genero.objects.filter(nome=row['nome']):
                    genero = Genero(    id=i+1,
                                        nome=row["nome"],

                                        )
                    genero.save()
                    print(i+1,row["nome"])




    def handle(self, *args, **options):
        self._create_genero()