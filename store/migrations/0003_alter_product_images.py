# Generated by Django 5.0.6 on 2024-05-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_alter_product_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="images",
            field=models.ImageField(upload_to="photos/products"),
        ),
    ]
