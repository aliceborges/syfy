# coding=utf-8

from django.shortcuts import redirect, render
from django.views import View


class HomeViews(View):
    template = 'index.html'

    def get(self, request, evento_id=None):
          return render(request,self.template,{})

