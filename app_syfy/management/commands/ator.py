# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from app_syfy.models.ator import Ator
import csv
#from django.
import hashlib

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "csv/ator.csv" na raiz do projeto.'
          
           ".'''


    def _create_autor(self):
        with open('csv/ator.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Ator.objects.filter(nome=row['nome']):
                    #pages = Page(category=Category.objects.get(name=row["category"]),
                    ator = Ator(
                        #category=Category.objects.get_or_create(name=row["category"])[0],
                                        nome=row["nome"],
                                      # url=row["url"],
                                      # views=row['views']


                                        )
                    ator.save()




    def handle(self, *args, **options):
        self._create_autor()
