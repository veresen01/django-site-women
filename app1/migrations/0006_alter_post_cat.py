# Generated by Django 5.0.6 on 2024-07-12 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_category_post_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.category'),
        ),
    ]
