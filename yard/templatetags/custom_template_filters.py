from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from yard.utils import get_image_data

register = template.Library()


@register.filter
@stringfilter
def space(value):
    return mark_safe("&nbsp;".join(value.split(' ')))


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter
def convert_to_kg(value):
    try:
        if value != 0 or value is not None:
            weight = value / 1000
            return weight
    except:
        return value

@register.filter
def convert_to_tonne(value):
    try:
        if value != 0 or value is not None:
            weight = value / 1000
            return weight
    except:
        return value


@register.filter
def to_base64(url):
    img_str = "data:image/png;base64, " + get_image_data(url)
    return img_str
    # return "data:image/png;base64, " + str(requests.get(url).content)

@register.filter
def count(item):
    s = 0
    for i in item:
        s += 1
    return s

@register.filter(name='display')
def display_value(bf):
    return dict(bf.field.choices).get(bf.data, '')