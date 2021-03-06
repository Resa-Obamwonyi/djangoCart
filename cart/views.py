from django.template.response import TemplateResponse
from .models import Product
from django.contrib import messages
from .forms import CartForm


def shopping_cart(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = CartForm(request.POST)
        new_dict = dict(form.data)
        new_dict.pop("csrfmiddlewaretoken")

        if form.is_valid():
            for product in new_dict:
                product_value = int(new_dict[product][0])
                product_instance = Product.objects.filter(name=product).first()

                if product_instance.quantity == 0:
                    return TemplateResponse(
                        request,
                        ["cart/cart.html"],
                        {
                            "products": products,
                            "message": messages.error(
                                request, f"Sorry, We are out of {product_instance.name}"
                            ),
                        },
                    )

                if product_value > product_instance.quantity:
                    return TemplateResponse(
                        request,
                        ["cart/cart.html"],
                        {
                            "products": products,
                            "message": messages.error(
                                request,
                                f"Sorry, We only have "
                                f"{product_instance.quantity}kg of "
                                f"{product_instance.name} left",
                            ),
                        },
                    )

            else:
                return TemplateResponse(
                    request,
                    ["cart/cart.html"],
                    {
                        "products": products,
                        "message": messages.success(
                            request, "Your order has been validated successfully"
                        ),
                    },
                )

    return TemplateResponse(request, ["cart/cart.html"], {"products": products})
