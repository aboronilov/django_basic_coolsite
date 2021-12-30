from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
from .models import Women, Category


def index(request):
    posts = Women.objects.all()

    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}

    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': 'О сайте'}
    return render(request, 'women/about.html', context=context)


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostForm()

    context = {'title': 'Добавление статьи',
               'form': form, }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse('<h1>Авторзация</h1>')


def read_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post_slug,
    }

    return render(request, 'women/post.html', context=context)


def read_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'title': 'Рубрики',
               'posts': posts,
               'cat_selected': cat_id}

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
