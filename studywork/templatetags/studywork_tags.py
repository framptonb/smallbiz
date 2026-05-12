from django import template
from django.template.defaultfilters import linebreaks
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def program_body(value):
    if not value:
        return ""

    text = str(value)

    # Let editors use simple markers inside Wagtail Localize.
    text = text.replace("[[p]]", "\n\n")
    text = text.replace("[[br]]", "\n")

    # Escape the actual text first for safety, then convert line breaks to HTML,
    # then mark only the generated paragraph/br HTML as safe.
    html = linebreaks(escape(text))

    return mark_safe(html)