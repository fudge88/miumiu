# Generated by Django 3.1.1 on 2020-10-13 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201013_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='comment',
        ),
    ]