# Generated by Django 5.0.6 on 2024-05-22 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clocks', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cart_item',
        ),
    ]