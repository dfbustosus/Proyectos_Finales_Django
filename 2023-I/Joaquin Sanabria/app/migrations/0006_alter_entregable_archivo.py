# Generated by Django 4.2 on 2023-05-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_estudiante_documento_alter_profesor_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='archivo',
            field=models.FileField(upload_to='media/'),
        ),
    ]