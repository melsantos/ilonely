# Generated by Django 2.1.2 on 2018-11-27 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_profile_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='products',
        ),
    ]