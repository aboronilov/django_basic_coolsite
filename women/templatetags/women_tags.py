from django import template
from women.models import Women, Category

register = template.Library()


@register.simple_tag(name='cats')
def get_categories(filter_pk=None):
    if filter:
        return Category.objects.filter(pk=filter_pk)
    else:
        return Category.objects.all()


@register.inclusion_tag('women/categories_list.html')
def show_categories(sort=None, cat_selected=0):
    if sort:
        cats = Category.objects.order_by(sort)
    else:
        cats = Category.objects.all()

    return {'cat_selected': cat_selected, 'cats': cats}


# @register.inclusion_tag('women/menu_list.html')
# def get_menu():
#     menu = [{'title': 'О сайте', 'url_name': 'about'},
#             {'title': 'Добавить статью', 'url_name': 'add_page'},
#             {'title': 'Обратная связь', 'url_name': 'contact'},
#             {'title': 'Войти', 'url_name': 'login'}]
#
#     return {'menu': menu}
