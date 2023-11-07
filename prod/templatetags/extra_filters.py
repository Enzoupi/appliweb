from django import template

register = template.Library()

@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

@register.filter
def get_attr(obj, attr_name):
    return getattr(obj, attr_name)

@register.filter
def extract_nth_values(dictionary, index):
    return [val[index] for val in dictionary.values()]

@register.filter
def dict_sum(dictionary):
    return sum(dictionary.values())
