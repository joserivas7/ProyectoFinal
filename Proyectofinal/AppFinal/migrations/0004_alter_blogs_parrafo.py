# Generated by Django 4.1.3 on 2023-01-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0003_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Parrafo',
            field=models.CharField(max_length=100),
        ),
    ]
