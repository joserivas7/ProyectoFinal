# Generated by Django 4.1.3 on 2023-01-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0035_alter_blogs_parrafoamplio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.CharField(max_length=20)),
                ('receptor', models.CharField(max_length=20)),
                ('cuerpo', models.CharField(max_length=50)),
            ],
        ),
    ]
