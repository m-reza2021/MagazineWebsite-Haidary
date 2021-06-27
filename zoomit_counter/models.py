from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from zoomit_posts.models import Post


class ViewCounter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

    def counter_view(self):
        return self.count()

    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدید ها'


