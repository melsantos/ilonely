# Generated by Django 2.1.2 on 2019-01-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190101_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentContent',
            field=models.CharField(max_length=150),
        ),
    ]