# Generated by Django 4.1.4 on 2023-01-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_articlegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlegallery',
            name='image',
            field=models.ImageField(upload_to='images/articles/articleGallery/', verbose_name='تصویر'),
        ),
    ]