# Generated by Django 4.1.3 on 2023-01-14 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0020_blogs_imagen_delete_blogsimagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='imagen',
        ),
    ]
