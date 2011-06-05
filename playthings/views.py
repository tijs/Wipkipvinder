from django.shortcuts import render_to_response
from django.template import RequestContext
from playthings.models import Plaything

def index(request):
    return render_to_response('playthings/index.html', {  }, context_instance=RequestContext(request))

def themap(request):
    return render_to_response('playthings/themap.html', {  }, context_instance=RequestContext(request))

def about(request):
    return render_to_response('playthings/about.html', {  }, context_instance=RequestContext(request))

def test(request, lat, lng, km):
    things = Plaything.objects.nearby(lat, lng, km)
    return render_to_response('playthings/test.html', { 'things' : things }, context_instance=RequestContext(request))
