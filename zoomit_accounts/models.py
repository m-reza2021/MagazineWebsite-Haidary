from django.db import models
from django.contrib.auth.models import User
from os.path import basename, splitext


# Create your models here.


def get_image_ext(file):
    base_name = basename(file)
    name, ext = splitext(base_name)
    return name, ext


def upload_path(instance, file):
    name, ext = get_image_ext(file)
    final_name = f'{instance.user}{ext}'
    return f'user/{final_name}'


class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path, default='/user/404.png')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'عکس کاربر'
        verbose_name_plural = 'عکس های کاربران'
