# Generated by Django 3.2.4 on 2021-07-01 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewcounter',
            options={'verbose_name': 'بازدید', 'verbose_name_plural': 'بازدید ها'},
        ),
    ]