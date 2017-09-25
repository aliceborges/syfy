# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import include, url

from app_syfy import views
from app_syfy.views import *
from django.views.generic.base import TemplateView

urlpatterns = [

    url(r'^$', HomeViews.as_view(), name='home'),

    #Ator
    url(r'^ator/cadastrar/$', AtorCreateView.as_view(), name='ator-add'),
    url(r'^ator/(?P<pk>[0-9]+)/visualizar/$', AtorDetailView.as_view(), name='ator-detail'),
    url(r'^ator/(?P<pk>[0-9]+)/editar/$', AtorUpdateView.as_view(), name='ator-update'),
    url(r'^ator/(?P<pk>[0-9]+)/excluir/$', AtorDeleteView.as_view(), name='ator-delete'),
    url(r'^ator/listar/$', AtorListView.as_view(), name='ator-list'),
    
    #Classificacao
    url(r'^classificacao/cadastrar/$', ClassificacaoCreateView.as_view(), name='classificacao-add'),
    url(r'^classificacao/(?P<pk>[0-9]+)/visualizar/$', ClassificacaoDetailView.as_view(), name='classificacao-detail'),
    url(r'^classificacao/(?P<pk>[0-9]+)/editar/$', ClassificacaoUpdateView.as_view(), name='classificacao-update'),
    url(r'^classificacao/(?P<pk>[0-9]+)/excluir/$', ClassificacaoDeleteView.as_view(), name='classificacao-delete'),
    url(r'^classificacao/listar/$', ClassificacaoListView.as_view(), name='classificacao-list'),

    #Genero
    url(r'^genero/cadastrar/$', GeneroCreateView.as_view(), name='genero-add'),
    url(r'^genero/(?P<pk>[0-9]+)/visualizar/$', GeneroDetailView.as_view(), name='genero-detail'),
    url(r'^genero/(?P<pk>[0-9]+)/editar/$', GeneroUpdateView.as_view(), name='genero-update'),
    url(r'^genero/(?P<pk>[0-9]+)/excluir/$', GeneroDeleteView.as_view(), name='genero-delete'),
    url(r'^genero/listar/$', GeneroListView.as_view(), name='genero-list'),

    #Video
    url(r'^video/cadastrar/$', VideoCreateView.as_view(), name='video-add'),
    url(r'^video/(?P<pk>[0-9]+)/visualizar/$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^video/(?P<pk>[0-9]+)/editar/$', VideoUpdateView.as_view(), name='video-update'),
    url(r'^video/(?P<pk>[0-9]+)/excluir/$', VideoDeleteView.as_view(), name='video-delete'),
     url(r'^video/listar/$', VideoListView.as_view(), name='video-list'),
    url(r'^video/listar/(?P<pk>[0-9]+)/$', VideoGeneroListView.as_view(), name='video-genero-list'),

    # ---- Usuario ----#
    url(r'^usuario/cadastrar/$', UsuarioCreateView.as_view(), name='usuario-add'),
    url(r'^usuario/(?P<pk>[0-9]+)/visualizar/$', UsuarioDetailView.as_view(), name='usuario-detail'),
    url(r'^usuario/listar/$', UsuarioListView.as_view(), name='usuario-list'),
    url(r'^usuario/editar/$', UsuarioUpdateView.as_view(), name='usuario-update'),
    # url(r'^login/$', login, {'template_name': 'index.html'}, name='login'),

    url(r'^video/busca/$', VideoListBuscaView.as_view(), name='busca'),
    #
    # url(r'^cadastro/$', TemplateView(template_name='usuario_form.html')),

    
]