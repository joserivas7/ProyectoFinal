# Generated by Django 4.1.3 on 2023-01-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0038_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='receptor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
