# Generated by Django 5.1.1 on 2024-10-08 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_bill_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
    ]
