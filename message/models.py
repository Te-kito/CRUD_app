from django.db import models
from blog.models import Post

# Create your models here.


class Message(models.Model):
    user = Post.author
    # ? classの関係性を表す
    # ? forignkey は　classに対して、一つだよ ManyToOne
    # ? ManyuToManyはメッセージとフレンドの関係は
    friends = models.ManyToManyField(user, blank=True)
    message_list =
