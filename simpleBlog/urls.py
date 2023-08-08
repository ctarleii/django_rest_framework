from django.contrib import admin
from django.urls import path, include

from posts.views import homepage

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path("posts/", include("posts.urls")),
    path('auth/', include('accounts.urls')),
]
