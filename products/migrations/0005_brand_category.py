# Generated by Django 4.2.7 on 2023-11-24 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_Category', to='products.category'),
        ),
    ]
