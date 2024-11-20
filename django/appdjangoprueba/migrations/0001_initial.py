# Generated by Django 5.1.3 on 2024-11-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.CharField(max_length=10)),
                ('descripcionProducto', models.CharField(max_length=255)),
                ('estatus', models.BooleanField()),
            ],
        ),
    ]
