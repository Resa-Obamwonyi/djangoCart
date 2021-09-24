from django import forms


class CartForm(forms.Form):
    Potatoes = forms.IntegerField()
    Onions = forms.IntegerField()
    Carrots = forms.IntegerField()