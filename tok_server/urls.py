__author__ = 'rt'
from django.conf.urls import include, url, patterns
from django.contrib import admin
from tok_server import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^(.*)$', views.index, name='index'),)