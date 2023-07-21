from django import template


register = template.Library()


@register.filter()
def character_limit(text):
    if len(text) > 20:
        return text[0:20] + '...'
    else:
        return text