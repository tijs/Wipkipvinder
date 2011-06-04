from django.conf.urls.defaults import *
from playthings.views import index, themap, about

urlpatterns = patterns('',
    url(r'^/?$', index, name="mob_home"),
    url(r'^themap?$', themap, name="mob_map"),
    url(r'^about?$', about, name="mob_about"),
)