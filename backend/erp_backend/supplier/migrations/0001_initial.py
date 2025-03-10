# Generated by Django 5.0.6 on 2024-07-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('contact_name', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
