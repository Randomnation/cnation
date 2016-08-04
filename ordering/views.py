from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django import forms
from products.models import Product
from .forms import OrderForm


def order_page(request):
    css3 = 'active'
    OrderForm.base_fields['products'] = forms.ModelChoiceField(queryset=Product.objects.all().order_by('prod_name'))
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render_to_response('ordering/orderSuccess.html')

    template = loader.get_template('ordering/order.html')
    context = RequestContext(request, {'form': form,
                                       })
    return HttpResponse(template.render(context))
