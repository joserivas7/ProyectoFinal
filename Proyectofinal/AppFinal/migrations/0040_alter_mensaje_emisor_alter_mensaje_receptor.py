# Generated by Django 4.1.3 on 2023-01-19 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFinal', '0039_mensaje_receptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL),
        ),
    ]
