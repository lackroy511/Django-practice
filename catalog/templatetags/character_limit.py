from django import template


register = template.Library()


@register.filter()
def character_limit(text):
    if len(text) > 100:
        return text[0:80] + '...'
    else:
        return text