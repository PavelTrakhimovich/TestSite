from django import template
from mainNews.models import *


register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('mainNews/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('mainNews/menu.html')
def show_menu():
    menu = [{'title':"About site", 'url_name': 'about'},
        {'title':"Add news", 'url_name': 'add_page'},
        {'title':"Feedback", 'url_name': 'contact'},
        {'title':"Sign In", 'url_name': 'login'},
        ]
    return {'menu': menu}