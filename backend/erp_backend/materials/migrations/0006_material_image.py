# Generated by Django 5.0.6 on 2024-07-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_material_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materials/'),
        ),
    ]
