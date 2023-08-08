from django.urls import path

from posts.views import *

urlpatterns = [
    path('homepage/', homepage, name='post_home'),
    path("", PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="post_detail"),
    path("current_user/", get_posts_for_current_user, name="current_user"),
    path("posts_for/", ListPostsForAuthor.as_view(), name="posts_for_current")

]
