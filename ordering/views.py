from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django import forms
from random import randint
from products.models import Product
from .forms import OrderForm


def order_gen(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return 'SO-' + str(randint(range_start, range_end))


def order_page(request):
    css3 = 'active'
    data = {'order_number': order_gen(6), 'user': request.user}
    OrderForm.base_fields['user'].widget = forms.HiddenInput()
    OrderForm.base_fields['order_number'].widget = forms.HiddenInput()
    OrderForm.base_fields['products'] = forms.ModelChoiceField(queryset=Product.objects.all().order_by('prod_name'))
    form = OrderForm(request.POST or None, initial=data)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render_to_response('ordering/orderSuccess.html')

    template = loader.get_template('ordering/order.html')
    context = RequestContext(request, locals())

    return HttpResponse(template.render(context))
