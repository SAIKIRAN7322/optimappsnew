# Generated by Django 5.1 on 2024-08-22 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('cost_price', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.shop')),
            ],
        ),
    ]