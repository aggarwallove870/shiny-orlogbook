
from django import template
  
register = template.Library()
  
@register.filter()
def low(dictionary,key):
    return dictionary.get(key)
    # print(dictionary.get(key))
    # pass