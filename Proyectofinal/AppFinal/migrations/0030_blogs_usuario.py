# Generated by Django 4.1.3 on 2023-01-16 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFinal', '0029_blogs_imagen_delete_imagenblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]