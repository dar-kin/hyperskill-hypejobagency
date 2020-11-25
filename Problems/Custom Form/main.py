from django import forms


class ProductForm(forms.Form):
    product = forms.CharField(min_length=3)
    quantity = forms.IntegerField()
    price = forms.FloatField()
