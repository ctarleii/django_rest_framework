from django.urls import path

from posts.views import PostListCreateView, PostRetrieveUpdateDeleteView, get_posts_for_current_user, ListPostsForAuthor

urlpatterns = [
    path("", PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="post_detail"),
    path("current_user/", get_posts_for_current_user, name="current_user"),
    path("posts_for/", ListPostsForAuthor.as_view(), name="posts_for_current")

]
