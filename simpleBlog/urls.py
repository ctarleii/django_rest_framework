from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('posts/', include(router.urls))
]
