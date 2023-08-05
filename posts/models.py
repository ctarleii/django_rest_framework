from django.contrib.auth import get_user_model
from django.db import models

"""
class Post:
    id int
    title str(50)
    content text
    created datetime
    author one to many
"""

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return f'{self.title}'
