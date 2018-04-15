import markdown
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@register.filter
@stringfilter
def mark2html(value):
    return markdown.markdown(value, extensions=['fenced_code', 'codehilite(css_class=highlight)', 'mdx_math'])

