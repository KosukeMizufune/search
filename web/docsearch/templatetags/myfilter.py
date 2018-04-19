import re

import markdown
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@register.filter
@stringfilter
def mark2html(value):
    return markdown.markdown(value, extensions=['fenced_code', 'codehilite(css_class=highlight)', 'mdx_math'])

@register.filter
@stringfilter
def get_filename(value):
    return re.findall(r'([^/]+?)?$', value)[0]
