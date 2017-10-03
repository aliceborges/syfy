"""syfy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from syfy import settings
from django.views.static import serve


def handle500(request):
    return render(request, '500.html', {})

def handle404(request):
    return render(request, '404.html', {})


def handle403(request):
    return render(request, '403.html', {})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', login, {'template_name': 'index.html'}, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app_syfy/index.html'), name='login'),
    url(r'^logout/$',  login_required(auth_views.LogoutView.as_view(template_name='app_syfy/index.html')), name='logout'),
    url(r'^media/(.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r"^", include('app_syfy.urls')),

    url(r'^', handle404, name='404'),
    url(r'^', handle403, name='403'),
    url(r'^', handle500, name='500'),
]