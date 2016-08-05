from django import forms
from .models import CustomerOrder


class OrderForm(forms.ModelForm):

    class Meta:
        model = CustomerOrder
        fields = ('user', 'products', 'notes', 'order_number')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['products', 'notes']
