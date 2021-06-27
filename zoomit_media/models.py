import os

from django.db import models

# Create your models here.

def get_image_ext(image):
    base_name = os.path.basename(image)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_path(instance, file):
    name, ext = get_image_ext(file)
    final_name = f'{instance.title}{ext}'
    return f'media/random_images/{final_name}'


class RandomImage(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=upload_path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'رسانه'
        verbose_name_plural = 'رسانه ها'