from django import template
register = template.Library()

@register.simple_tag()
def total(cart):
    total = 0
    for item in cart:
        total += item.quantity * item.book.price
    return total

@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * unit_price

