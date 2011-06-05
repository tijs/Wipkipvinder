from django.conf.urls.defaults import *
from views import index
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^public/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': 'public/'}),
    url(r'^/?$', index, name="homepage"),
    url(r'^play/', include('playthings.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
