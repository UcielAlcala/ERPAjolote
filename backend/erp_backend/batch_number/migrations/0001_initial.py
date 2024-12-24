# Generated by Django 5.0.6 on 2024-07-13 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sku', '0003_alter_sku_code_alter_sku_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(blank=True, max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batches', to='sku.sku')),
            ],
        ),
    ]