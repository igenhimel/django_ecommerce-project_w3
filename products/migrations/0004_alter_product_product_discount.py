# Generated by Django 4.2.4 on 2023-08-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
