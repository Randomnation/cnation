from django.shortcuts import render_to_response
from django.template import RequestContext


def order_page(request):
    css3 = 'active'
    return render_to_response('ordering/order.html', locals(), context_instance=RequestContext(request))
