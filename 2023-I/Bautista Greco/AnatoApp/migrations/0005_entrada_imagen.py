# Generated by Django 4.2 on 2023-05-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnatoApp', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='entradas/'),
        ),
    ]
