# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.classificacao import Classificacao
from app_syfy.forms.classificacao import ClassificacaoForm


class ClassificacaoListView(ListView):
    queryset = Classificacao.objects.all()


class ClassificacaoDetailView(DetailView):
    queryset = Classificacao.objects.filter(excluido=False)


class ClassificacaoCreateView(CreateView):
    model = Classificacao
    form_class = ClassificacaoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ClassificacaoCreateView, self).form_valid(form)


class ClassificacaoUpdateView(UpdateView):
    model = Classificacao
    form_class = ClassificacaoForm
    # form_class = ClassificacaoEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ClassificacaoUpdateView, self).form_valid(form)


class ClassificacaoDeleteView(DeleteView):
    queryset = Classificacao.objects.filter(excluido=False)
    success_url = reverse_lazy('classificacao-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ClassificacaoDeleteView, self).form_valid(form)
