# Generated by Django 5.0.6 on 2024-07-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalproduct',
            name='total_cost',
            field=models.FloatField(default=0.0),
        ),
    ]
