from django.db import models


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان برچسب')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در آدرس')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسبها'

    def __str__(self):
        return self.title

    def get_tag_url(self):
        return f'/posts/tag/{self.title}'
