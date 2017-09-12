# coding=utf-8

from django.shortcuts import redirect, render
from django.views import View
from app_syfy.models.video import *

class HomeViews(View):
    template = 'app_syfy/index.html'

    def get(self, request):
          videos_genero={}
          videos=Video.objects.all()
          try:
              videos_genero["acao"]=videos.filter(genero__pk=1)[:4]
              videos_genero["animacao"]=videos.filter(genero__pk=2)[:4]
              videos_genero["drama"]=videos.filter(genero__pk=12)[:4]
              videos_genero["ficcao"]=videos.filter(genero__pk=16)[:4]
              video=videos.order_by('-id')[0]
          except:
              video=""
          #print(videos_genero)
          return render(request,self.template,{"videos_genero":videos_genero,'video':video})
