from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    """ Returns True if the length of the value is the same as the argument """
    return len(value) == int(arg)
