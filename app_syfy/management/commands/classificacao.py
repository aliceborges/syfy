# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from app_syfy.models.classificacao import Classificacao
import csv
#from django.
import hashlib

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "csv/classificacao.csv" na raiz do projeto.'
          
           ".'''


    def _create_classificacao(self):
        with open('csv/classificacao.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Classificacao.objects.filter(classificacao=row['classificacao']):
                    #pages = Page(category=Category.objects.get(name=row["category"]),
                    classificacao = Classificacao(
                        #category=Category.objects.get_or_create(name=row["category"])[0],
                                        classificacac=row["classificacao"],
                                      # url=row["url"],
                                      # views=row['views']


                                        )
                    classificacao.save()




    def handle(self, *args, **options):
        self._create_classificacao()
