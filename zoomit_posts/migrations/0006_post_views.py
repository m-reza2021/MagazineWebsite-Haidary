# Generated by Django 3.2.4 on 2021-06-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_posts', '0005_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
