# Generated by Django 4.2 on 2023-04-29 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_curso_costo_alter_curso_jornada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='cursos',
            new_name='curso',
        ),
    ]