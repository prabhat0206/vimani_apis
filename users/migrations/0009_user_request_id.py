# Generated by Django 4.0.1 on 2022-07-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_last_otp_ph_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='request_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]