# Generated by Django 4.1.4 on 2023-01-07 08:59

import apps.articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_articlegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlegallery',
            name='image',
            field=models.ImageField(upload_to=apps.articles.models.get_member_upload_to, verbose_name='تصویر'),
        ),
    ]
