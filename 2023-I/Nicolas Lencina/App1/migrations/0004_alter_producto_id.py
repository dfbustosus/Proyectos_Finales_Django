# Generated by Django 4.2 on 2023-05-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_producto_imagen_vendedor_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]