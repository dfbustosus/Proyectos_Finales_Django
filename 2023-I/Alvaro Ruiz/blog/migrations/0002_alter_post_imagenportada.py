# Generated by Django 4.2 on 2023-05-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagenPortada',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]