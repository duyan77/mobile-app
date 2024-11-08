from django import template
from babel.numbers import format_currency

register = template.Library()


@register.filter
def currency(value):
	return format_currency(value, 'VND', locale='vi_VN')
