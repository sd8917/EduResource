# Generated by Django 3.1.4 on 2020-12-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201230_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files'),
        ),
    ]