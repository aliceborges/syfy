# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.usuario import Usuario
from app_syfy.forms.usuario import UsuarioForm


class UsuarioListView(ListView):
    queryset = Usuario.objects.all()


class UsuarioDetailView(DetailView):
    queryset = Usuario.objects.all()


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioCreateView, self).form_valid(form)


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    # form_class = UsuarioEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioUpdateView, self).form_valid(form)


class UsuarioDeleteView(DeleteView):
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('usuario-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioDeleteView, self).form_valid(form)