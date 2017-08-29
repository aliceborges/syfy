# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.autor import Autor
from app_syfy.forms.autor import AutorForm


class AutorListView(ListView):
    queryset = Autor.objects.all()


class AutorDetailView(DetailView):
    queryset = Autor.objects.filter(excluido=False)


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AutorCreateView, self).form_valid(form)


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    # form_class = AutorEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AutorUpdateView, self).form_valid(form)


class AutorDeleteView(DeleteView):
    queryset = Autor.objects.filter(excluido=False)
    success_url = reverse_lazy('autor-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AutorDeleteView, self).form_valid(form)
