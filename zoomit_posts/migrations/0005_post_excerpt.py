# Generated by Django 3.2.4 on 2021-06-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_posts', '0004_auto_20210620_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=255, null=True, verbose_name='چکیده'),
        ),
    ]
