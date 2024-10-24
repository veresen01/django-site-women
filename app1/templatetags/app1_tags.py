from django import template
from django.db.models import Count

import app1.views as views
from app1.models import Category, TagPost
from app1.utils import menu

register = template.Library()


# @register.simple_tag(name='getcats')
# def get_categories():
#     return views.cats_db


@register.simple_tag
def get_menu():
    return menu

@register.inclusion_tag('app1/list_categories.html')
def show_categories(cat_selected=0):
    # cats = views.cats_db
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('app1/list_tags.html')
def show_all_tags():
    def show_categories(cat_selected_id=0):
        cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
        return {"cats": cats, "cat_selected": cat_selected_id}