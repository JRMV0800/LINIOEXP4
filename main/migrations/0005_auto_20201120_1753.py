# Generated by Django 3.1.2 on 2020-11-20 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_producto_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoimage',
            name='image',
        ),
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]