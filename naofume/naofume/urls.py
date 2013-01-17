# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from profiles import views as pviews
from social.views import HistoryView, WallView
from shortener.shortener import ShortenerView
from django.views.generic.simple import redirect_to
from calc.calc import Calc
from calc.stats import StatsView

urlpatterns = patterns('',
    url(r'^favicon.ico$',  redirect_to, {'url': '/static/img/favicon.ico'}),
    url(r'^$', pviews.Home.as_view(), name='home'),
    url(r'^login/$', pviews.Login.as_view(), name='login'),
    url(r'^excluir/$', pviews.excluir, name='login'),
    url(r'^amigos/$', pviews.friends, name='friends'),
    url(r'^registrar/$', 'profiles.views.register', name='register',kwargs={'edit': False}),
    url(r'^editar/$', 'profiles.views.register', name='edit',kwargs={'edit': True}),
    url(r'^logout/$', 'profiles.views.logout', name='logout'),
    url(r'^sobre/$', 'profiles.views.about', name='about'),
    url(r'^termos/$', 'profiles.views.privacy', name='termos'),
    url(r'^midia-kit/$', 'profiles.views.midia', name='midia'),
    # POST para adicionar um novo UserHistory
    url(r'^historico/$', HistoryView.as_view()),
    url(r'^post$', WallView.as_view()),

    # encurtador de urls 
    url(r'^p/(?P<code>[0-9a-f]+)$', ShortenerView.as_view(), {'type': "post"}),
    url(r'^h/(?P<code>[0-9a-f]+)$', ShortenerView.as_view(), {'type': "history"}),

    # Calculadora de estatísticas para parar de fumar
    url(r'^calculadora/', Calc.as_view()),


    url(r'^(?P<nickname>[0-9a-zA-Z-_\.]+)/$', 'profiles.views.profile', name='profile'),

    url(r'^(?P<nickname>[0-9a-zA-Z-_\.]+)/(?P<id>\d+)/$',
        'social.views.post', name='post'),

    # chamadas a api de statísticas de usuário (ajax)
    url(r'^estatistica/(?P<method>[a-z0-9]+)/(?P<nickname>[0-9a-zA-Z-_\.]+)?$', StatsView.as_view()),

    # Tela de estatísticas do usuário no perfil
    url(r'^(?P<nickname>[0-9a-zA-Z-_\.]+)/estatistica/', StatsView.as_view(), {'method': "user"})
)
