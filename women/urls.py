from django.urls import path, re_path

from .views import WomenHome, about, ShowCategory, ReadPost, AddPost, RegisterUser, LoginUser, logout_user, ShowContact

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('add/', AddPost.as_view(), name='add_page'),
    path('contact/', ShowContact.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ReadPost.as_view(), name='read_post'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='read_category'),
]

