from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Product

# Create your views here.
def shopping_cart(request):
    return TemplateResponse(request, ['cart/cart.html'], {'products': Product.objects.all()})