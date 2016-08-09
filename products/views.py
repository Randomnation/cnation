from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Product


def products_page(request):
    css2 = 'active'
    prod = Product.objects.all()
    return render_to_response('products/products.html', locals(), context_instance=RequestContext(request))
