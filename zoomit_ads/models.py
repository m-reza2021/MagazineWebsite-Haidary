from django.db import models
import os

# Create your models here.


def get_image_ext(image):
    base_name = os.path.basename(image)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_path(instance, file):
    name, ext = get_image_ext(file)
    final_name = f'{instance.title}{ext}'
    return f'ads/{final_name}'


class Advertise(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    link = models.URLField(max_length=255, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to=upload_path, verbose_name='تصویر')

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return self.title
