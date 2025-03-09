from django import template

register = template.Library()

@register.filter(name='abs_value')
def abs_value(value):
    try:
        return abs(value)
    except TypeError:
        return value  # If value is not numeric, return it as-is
