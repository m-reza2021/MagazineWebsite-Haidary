from django.db import models
from django.contrib.auth.models import User
import os
from jalali_date import date2jalali, datetime2jalali
from ckeditor.fields import RichTextField


# Create your models here.
from django.db.models import Q

from zoomit_categories.models import Category
from zoomit_tags.models import Tag


def get_image_ext(image):
    base_name = os.path.basename(image)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_path(instance, file):
    name, ext = get_image_ext(file)
    final_name = f'{instance.title}{ext}'
    return f'posts/{final_name}'


class PostManager(models.Manager):
    def get_product_by_id(self, post_id):
        return self.get_queryset().filter(id=post_id).first()

    def get_posts_by_category(self, category_name):
        return self.get_queryset().filter(category__slug=category_name).distinct()

    def get_posts_by_tag(self, tag_name):
        return self.get_queryset().filter(tags__title=tag_name).distinct()

    def search_posts(self, query):

        search_query = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__title__iexact=query) |
            Q(tags__title__iexact=query)
        )

        return self.get_queryset().filter(search_query).distinct()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    excerpt = models.CharField(max_length=255, null=True, verbose_name='چکیده')
    # description = models.TextField(null=True, blank=True, verbose_name='شرح')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=upload_path, verbose_name='تصویر')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    issue_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0, editable=False)


    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    objects = PostManager()

    def author_name(self):
        return self.author.get_full_name()

    def get_absolute_url(self):
        return f'/post/{self.id}/{self.title.replace(" ","-")}'

    def get_issue_date(self):
        return date2jalali(self.issue_date)
