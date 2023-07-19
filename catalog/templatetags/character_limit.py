from django import template


register = template.Library()


@register.filter()
def character_limit(text):
    if len(text) > 70:
        return text[0:68] + '...'
    else:
        return text