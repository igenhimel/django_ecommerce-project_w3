# Generated by Django 4.2.4 on 2023-08-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_details', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
