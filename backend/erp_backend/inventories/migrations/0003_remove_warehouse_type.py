# Generated by Django 5.0.6 on 2024-07-17 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0002_inventoryitem_batch_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='type',
        ),
    ]
