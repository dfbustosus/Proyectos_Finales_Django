# Generated by Django 3.2.7 on 2021-10-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211010_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]