import markdown
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@register.filter
def mark2html(value):
    return markdown.markdown(value)

