# Generated by Django 4.1.4 on 2023-01-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articlegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlegallery',
            name='image',
            field=models.ImageField(upload_to='images/articles/article-', verbose_name='تصویر'),
        ),
    ]
