# Generated by Django 5.0.6 on 2024-07-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
