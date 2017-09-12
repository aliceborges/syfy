# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404, request
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models import Genero
from app_syfy.models.video import Video
from app_syfy.forms.video import VideoForm


class VideoListView(ListView):
    queryset = Video.objects.all()

class VideoGeneroListView(ListView):
    queryset = Video.objects.all()
    paginate_by = 10
    # template_name = "app_syfy/video_list.html"

    def get_queryset(self):
            print(self.request.user.id)
            queryset = Video.objects.filter(genero__pk=self.kwargs['pk'])
            return queryset
    def get_context_data(self, **kwargs):
        context = super(VideoGeneroListView, self).get_context_data(**kwargs)
        context['genero'] = Genero.objects.get(pk=self.kwargs['pk'])
        return context
class VideoDetailView(DetailView):
    queryset = Video.objects.all()


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm

    # def form_valid(self, form):
    #     self.object = Video(arquivo=self.get_form_kwargs().get('files')['arquivo'])
        # self.object = form.save(commit=False)
        # self.object.save()
        # return super(VideoCreateView, self).form_valid(form)
        # self.id = self.object.id

        # return HttpResponseRedirect(self.get_success_url())

    # def get_success_url(self):
    #     return reverse('video-detail', kwargs={'pk': 1})


class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    # form_class = VideoEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(VideoUpdateView, self).form_valid(form)


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = reverse_lazy('video-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(VideoDeleteView, self).form_valid(form)

