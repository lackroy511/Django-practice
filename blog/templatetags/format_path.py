from django import template


register = template.Library()


@register.filter()
def format_path(text):
    return f'/media/{text}' 