from django.conf.urls import url, patterns, include

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blog/(?P<id>\d+)/$', views.detail, name='detail'),
            ]