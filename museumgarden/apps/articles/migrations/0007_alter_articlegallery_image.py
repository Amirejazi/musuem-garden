# Generated by Django 4.1.4 on 2023-01-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlegallery',
            name='image',
            field=models.ImageField(upload_to='images/articles/articles.Article.id', verbose_name='تصویر'),
        ),
    ]
