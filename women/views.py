from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import Women, Category

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#
#     context = {'title': 'Главная страница',
#                'posts': posts,
#                'cat_selected': 0}
#
#     return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': 'О сайте'}
    return render(request, 'women/about.html', context=context)


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление поста'
        context['menu'] = menu
        return context


# def add_page(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {'title': 'Добавление статьи',
#                'form': form, }
#     return render(request, 'women/addpage.html', context=context)


def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse('<h1>Авторзация</h1>')


class ReadPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

# def read_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post_slug,
#     }
#
#     return render(request, 'women/post.html', context=context)


class ShowCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['posts'][0].cat_id
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def read_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'title': 'Рубрики',
#                'posts': posts,
#                'cat_selected': cat_id}
#
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
