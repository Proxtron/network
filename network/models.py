from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    message = models.CharField(max_length=1000, default='')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True)
    timePosted = models.DateTimeField(auto_now_add=True)
    likeCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author.username} posted the message: {self.message} at {self.timePosted}"