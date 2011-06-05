from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import PlaythingsHandler
#from django.views.decorators.cache import cache_control

#cached_resource = cache_control(static_root=True, maxage=30, s_maxage=300) # cache resource (when enabled)
play_resource = Resource(handler=PlaythingsHandler)

urlpatterns = patterns('',
    #url(r'^all\.(?P<emitter_format>.+)$', play_handler),
    url(r'^nearby/(?P<lat>.+)/(?P<lng>.+)/(?P<km>.+)\.(?P<emitter_format>.+)$', play_resource),
)