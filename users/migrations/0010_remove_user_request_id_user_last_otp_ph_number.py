# Generated by Django 4.0.1 on 2022-07-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_request_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='request_id',
        ),
        migrations.AddField(
            model_name='user',
            name='last_otp_ph_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
