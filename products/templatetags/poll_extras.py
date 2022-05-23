from django import template
from django.template.defaultfilters import stringfilter

from products.models import Cart

register = template.Library()


@register.filter
@stringfilter
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[1]


def get_lang(value, key):
    return value.split(key)[1]


def calc_cart_total(key):
    cart_pro = Cart.objects.all()
    sum = 0
    for p in cart_pro:
        sum += (p.product_quantity * p.product.price)
    return sum


def calc_product_total(quantity, price):
    return (quantity * price)


register.filter('split', split)
register.filter('get_lang', get_lang)
register.filter('calc_cart_total', calc_cart_total)
register.filter('calc_product_total', calc_product_total)
