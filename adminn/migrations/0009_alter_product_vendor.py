# Generated by Django 4.0.1 on 2022-07-13 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminn', '0008_rename_reviewer_message_review_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='of_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
