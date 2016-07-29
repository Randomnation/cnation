from django.shortcuts import render_to_response
from django.template import RequestContext


def main_page(request):
    css1 = 'active'
    return render_to_response('main/index.html', locals(), context_instance=RequestContext(request))


def contact_page(request):
    css3 = 'active'
    return render_to_response('main/contact.html', locals(), context_instance=RequestContext(request))
