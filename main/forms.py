from django import forms
from .models import Order

class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address']
