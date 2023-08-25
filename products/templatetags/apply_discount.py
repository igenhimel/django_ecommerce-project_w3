from django import template

register = template.Library()


@register.simple_tag
def apply_discount(product_price, product_discount):
    try:
        price = float(product_price)
        discount_percentage = int(product_discount)
        discounted_price = price - (price * (discount_percentage / 100))
        # Format the result to two decimal places
        return f"{discounted_price:.2f}"
    except (ValueError, TypeError):
        return ""
