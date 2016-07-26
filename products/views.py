from django.shortcuts import render_to_response
from django.template import RequestContext


def products_page(request):
    css2 = 'active'
    return render_to_response('products/products.html', locals(), context_instance=RequestContext(request))
