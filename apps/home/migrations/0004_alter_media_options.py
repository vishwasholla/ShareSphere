# Generated by Django 3.2.6 on 2023-12-11 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_media_shared_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ('-id',)},
        ),
    ]
