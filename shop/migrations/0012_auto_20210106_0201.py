# Generated by Django 3.1.4 on 2021-01-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='failed', max_length=200),
        ),
    ]
