# Generated by Django 3.1.2 on 2020-11-19 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_producto_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='slug',
        ),
    ]