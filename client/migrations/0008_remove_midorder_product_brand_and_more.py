# Generated by Django 4.0.1 on 2022-05-30 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_midorder_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midorder',
            name='product_brand',
        ),
        migrations.RemoveField(
            model_name='midorder',
            name='product_color',
        ),
        migrations.RemoveField(
            model_name='midorder',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='midorder',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='midorder',
            name='unit_size',
        ),
    ]
