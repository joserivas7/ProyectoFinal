# Generated by Django 4.1.3 on 2023-01-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0033_delete_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='parrafoamplio',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]