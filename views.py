from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from is_mobile import is_mobile
from django.core.urlresolvers import reverse

def index(request):
    if is_mobile(request):
        return HttpResponseRedirect(reverse('mob_home'))
    else:
        return render_to_response('index.html', {  }, context_instance=RequestContext(request))
