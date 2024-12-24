# Generated by Django 5.0.6 on 2024-07-04 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_material_description'),
        ('printed_pieces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printedpiecematerial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.material'),
        ),
    ]
