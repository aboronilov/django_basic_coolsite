from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', read_post, name='read_post'),
]
