# Generated by Django 3.2.12 on 2023-09-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20230915_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user_is_approved',
            field=models.BooleanField(default=False),
        ),
    ]