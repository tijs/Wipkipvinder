from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 

def index(request):
  return render_to_response('index.html', {  }, context_instance=RequestContext(request))
    
def themap(request):
  return render_to_response('themap.html', {  }, context_instance=RequestContext(request))
