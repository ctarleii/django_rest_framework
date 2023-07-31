from django.urls import path

from .views import *


urlpatterns = [
    path('homepage/', homepage, name='posts_home'),
    path('', list_posts, name='posts_list'),
]
