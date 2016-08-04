from django import forms
from .models import CustomerOrder


class OrderForm(forms.ModelForm):

    class Meta:
        model = CustomerOrder
        fields = ('user', 'notes', 'products', 'order_number')
