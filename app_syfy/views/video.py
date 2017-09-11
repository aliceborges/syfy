# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404, request
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic import *

from app_syfy.models.video import Video
from app_syfy.forms.video import VideoForm


class VideoListView(ListView):
    queryset = Video.objects.all()


class VideoDetailView(DetailView):
    queryset = Video.objects.all()


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm

    def form_valid(self, form):
        self.object = Video(arquivo=self.get_form_kwargs().get('files')['arquivo'])
        self.object = form.save(commit=False)
        self.object.save()
        # return super(VideoCreateView, self).form_valid(form)
        self.id = self.object.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.id})


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

