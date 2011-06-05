from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import PlaythingsHandler
from django.views.decorators.cache import cache_control

cached_resource = cache_control(static_root=True, maxage=300, s_maxage=3000) # cache resource (when enabled)
play_resource = cached_resource(Resource(handler=PlaythingsHandler))

urlpatterns = patterns('',
    #url(r'^all\.(?P<emitter_format>.+)$', play_handler),
    url(r'^nearby/(?P<lat>.+)/(?P<lng>.+)/(?P<km>.+)\.(?P<emitter_format>.+)$', play_resource),
)