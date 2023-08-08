from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from posts.models import Post


class OwnerOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_superuser)


class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, view, obj: Post):
        return bool(
            request.method in SAFE_METHODS or
            request.user == obj.author
        )
