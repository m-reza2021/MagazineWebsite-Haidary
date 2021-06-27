from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from zoomit_posts.models import Post


class SaveList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'دخیره شده ها'

    def __str__(self):
        return self.post.title

