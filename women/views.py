from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import Women, Category
from .utils import DataMixin


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'О сайте', 'page_obj': page_obj}
    return render(request, 'women/about.html', context=context)


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление поста')
        return context | c_def


class ShowContact(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ReadPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


class ShowCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')