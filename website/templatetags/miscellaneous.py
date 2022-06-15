from django import template
import datetime


register = template.Library()

@register.simple_tag
def year():
    return datetime.date.today().year
