# Generated by Django 4.0.1 on 2022-05-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='in_stock',
            field=models.IntegerField(default=100),
        ),
    ]
