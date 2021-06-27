from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در آدرس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/posts/category/{self.slug}'
