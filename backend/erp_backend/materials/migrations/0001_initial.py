# Generated by Django 5.0.6 on 2024-07-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Producción', 'Producción'), ('Empaque', 'Empaque'), ('Envío', 'Envío')], max_length=50)),
                ('sub_type', models.CharField(choices=[('Filamento', 'Filamento'), ('Insumos', 'Insumos'), ('Refacciones', 'Refacciones'), ('Pegamento', 'Pegamento')], max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('cost_per_unit', models.FloatField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
