# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import include, url
from app_syfy.views.home import HomeViews
urlpatterns = [

    url(r'^$', HomeViews.as_view(), name='home'),

]