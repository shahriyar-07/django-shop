from django import template
from jdatetime import date
from re import sub

register = template.Library()

@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    return date.fromgregorian(date=value)

@register.filter(name='three_digits_currency')
def three_digits_currency(value:int):
    return '{:,}'.format(value) + " تومان"

@register.simple_tag
def multiply(quantity , price , *args , **kwargs):
    return three_digits_currency(quantity * price)


@register.filter(name='three_digits_currency_str')
def three_digits_currency_str(text):
    return sub(r"(?<=\d)(?=(\d{3})+$)", ",", text)
