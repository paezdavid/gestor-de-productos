# Generated by Django 3.2.12 on 2023-09-18 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20230918_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagenes',
        ),
    ]
