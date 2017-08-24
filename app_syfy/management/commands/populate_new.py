# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from rangoapp.models import *
import csv
#from django.
import hashlib

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "csv/aginas.csv" na raiz do projeto.'
           Deve conter os cabeçalhos:
           "category",
           "title",
           "url",
           "views"
           ".'''


    def _create_category(self):
        with open('csv/category.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Category.objects.filter(name=row['name']):
                    category = Category(
                        # category=Category.objects.get(name=row["category"]),
                                        name=row["name"],
                                        views=row["views"],
                                        likes=row["likes"],
                                        # url=row["url"],
                                        # views=row['views']

                                        )
                    category.save()

    def _create_page(self):
        with open('csv/page.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Page.objects.filter(title=row['title']):
                    #pages = Page(category=Category.objects.get(name=row["category"]),
                    pages = Page(category=Category.objects.get_or_create(name=row["category"])[0],
                                        title=row["title"],
                                        url=row["url"],
                                        views=row['views']

                                        )
                    pages.save()




    def handle(self, *args, **options):
        self._create_category()
        self._create_page()
