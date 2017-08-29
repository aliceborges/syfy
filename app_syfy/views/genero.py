# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.genero import Genero
from app_syfy.forms.genero import GeneroForm


class GeneroListView(ListView):
    queryset = Genero.objects.all()


class GeneroDetailView(DetailView):
    queryset = Genero.objects.filter(excluido=False)


class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(GeneroCreateView, self).form_valid(form)


class GeneroUpdateView(UpdateView):
    model = Genero
    form_class = GeneroForm
    # form_class = GeneroEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(GeneroUpdateView, self).form_valid(form)


class GeneroDeleteView(DeleteView):
    queryset = Genero.objects.filter(excluido=False)
    success_url = reverse_lazy('genero-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(GeneroDeleteView, self).form_valid(form)
