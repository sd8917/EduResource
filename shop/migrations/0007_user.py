# Generated by Django 3.1.4 on 2020-12-31 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
