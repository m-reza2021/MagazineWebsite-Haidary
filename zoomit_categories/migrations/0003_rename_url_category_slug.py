# Generated by Django 3.2.4 on 2021-06-19 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_categories', '0002_alter_category_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='URL',
            new_name='slug',
        ),
    ]
