# Generated by Django 3.1.1 on 2020-10-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
