# Generated by Django 2.1.2 on 2019-01-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='isRequest',
            field=models.BooleanField(),
        ),
    ]
