# Generated by Django 4.2 on 2023-05-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_imagenportada_postimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]