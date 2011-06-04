from django.shortcuts import render_to_response
from django.template import RequestContext 

def index(request):
    return render_to_response('playthings/index.html', {  }, context_instance=RequestContext(request))

def themap(request):
    return render_to_response('playthings/themap.html', {  }, context_instance=RequestContext(request))

def about(request):
    return render_to_response('playthings/about.html', {  }, context_instance=RequestContext(request))
