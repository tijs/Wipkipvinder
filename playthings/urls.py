from django.conf.urls.defaults import *

urlpatterns = patterns('playthings.views',
    url(r'^/?$', 'index', name="mob_home"),
    url(r'^themap?$', 'themap', name="mob_map"),
    url(r'^about?$', 'about', name="mob_about"),
    url(r'^test/(?P<lat>.+)?/(?P<lng>.+)?/(?P<km>\d+)?$', 'test', name="test"),
)