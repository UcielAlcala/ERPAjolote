# Generated by Django 5.0.6 on 2024-07-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printed_pieces', '0003_printedpiece_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printedpiece',
            name='sku',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
