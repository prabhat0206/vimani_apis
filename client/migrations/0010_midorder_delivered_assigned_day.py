# Generated by Django 4.0.1 on 2022-06-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_rename_pid_midorder_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='midorder',
            name='delivered_assigned_day',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
