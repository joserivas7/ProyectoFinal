# Generated by Django 4.1.3 on 2023-01-16 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0030_blogs_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='usuario',
        ),
    ]
