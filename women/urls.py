from django.urls import path, re_path

from .views import WomenHome, contact, login, about, ShowCategory, ReadPost, AddPost

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('add/', AddPost.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ReadPost.as_view(), name='read_post'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='read_category'),
]
