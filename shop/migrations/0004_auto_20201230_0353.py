# Generated by Django 3.1.4 on 2020-12-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201230_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='uploads/thumbnails'),
        ),
    ]
