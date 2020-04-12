from django import template

register = template.Library()

@register.filter
def learntags(value, arg):
	return value + str(arg)