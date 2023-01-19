from django import forms

class ProductsForm(forms.Form):
    Pname = forms.CharField(max_length=100, label="Product Name")
    Price = forms.FloatField( label="Price")
    Stock = forms.IntegerField( label="Stock")