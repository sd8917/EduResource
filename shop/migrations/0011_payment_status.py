# Generated by Django 3.1.4 on 2021-01-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210106_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
