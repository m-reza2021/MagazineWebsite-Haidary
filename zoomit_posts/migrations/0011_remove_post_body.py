# Generated by Django 3.2.4 on 2021-07-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_posts', '0010_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
