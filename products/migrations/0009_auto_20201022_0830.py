# Generated by Django 3.1.1 on 2020-10-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201019_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.CharField(max_length=250),
        ),
    ]
