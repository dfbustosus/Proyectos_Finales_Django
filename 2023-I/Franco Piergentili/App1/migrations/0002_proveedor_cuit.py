# Generated by Django 4.2 on 2023-05-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='cuit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
