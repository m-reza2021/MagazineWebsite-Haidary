from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from zoomit_posts.models import Post


class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    user_image = models.CharField(max_length=255, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class UserCommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(UserComment, on_delete=models.CASCADE)
    body = models.TextField()
    user_image = models.CharField(max_length=255, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'جواب'
        verbose_name_plural = 'جواب ها'
