# Generated by Django 3.2.4 on 2021-07-01 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_accounts', '0002_alter_profileimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileimage',
            options={'verbose_name': 'عکس کاربر', 'verbose_name_plural': 'عکس های کاربران'},
        ),
    ]
