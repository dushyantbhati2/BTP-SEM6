# Generated by Django 5.1.5 on 2025-04-13 17:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_farmerprofile_qr_code_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='screenshot',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='screenshot'),
        ),
    ]
