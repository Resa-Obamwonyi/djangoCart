from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import Product
from django.contrib import messages
from .forms import CartForm
from django.shortcuts import render


def shopping_cart(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            for product in form.cleaned_data:
                product_instance = Product.objects.filter(name=product).first()
                if form.cleaned_data[product] > product_instance.quantity:
                        return TemplateResponse(request, ['cart/cart.html'], 
                        {'products': products, 
                        'message':messages.error(request, f'Sorry, We only have {product_instance.quantity}kg of {product_instance.name} left')})
        
            else:
                return TemplateResponse(request, ['cart/cart.html'],
                {'products': products, 
                'message': messages.success(request, 'Your order has been validated successfully')})

    return TemplateResponse(request, ['cart/cart.html'], {'products': products})
