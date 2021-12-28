from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts,
               'cats': cats,
               'cat_selected': 0}

    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': 'О сайте',
               'menu': menu}
    return render(request, 'women/about.html', context=context)


def add_page(request):
    return HttpResponse('<h1>Добавление статьи</h1>')


def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse('<h1>Авторзация</h1>')


def read_post(request, post_id):
    return HttpResponse(f'<h1>Чтение статьи с номером {post_id}</h1>')


def read_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {'title': 'Рубрики',
               'menu': menu,
               'posts': posts,
               'cats': cats,
               'cat_selected': cat_id}

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
