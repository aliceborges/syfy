# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.ator import Ator
from app_syfy.forms.ator import AtorForm


class AtorListView(ListView):
    queryset = Ator.objects.all()


class AtorDetailView(DetailView):
    queryset = Ator.objects.all()


class AtorCreateView(CreateView):
    model = Ator
    form_class = AtorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AtorCreateView, self).form_valid(form)


class AtorUpdateView(UpdateView):
    model = Ator
    form_class = AtorForm
    # form_class = AtorEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AtorUpdateView, self).form_valid(form)


class AtorDeleteView(DeleteView):
    queryset = Ator.objects.all()
    success_url = reverse_lazy('ator-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(AtorDeleteView, self).form_valid(form)
