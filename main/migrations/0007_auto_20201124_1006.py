# Generated by Django 3.1.2 on 2020-11-24 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201120_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='reputacion',
            new_name='Reputacion',
        ),
    ]