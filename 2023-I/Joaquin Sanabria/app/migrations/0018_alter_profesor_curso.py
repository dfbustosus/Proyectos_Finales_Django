# Generated by Django 4.2.1 on 2023-05-13 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesores', to='app.curso'),
        ),
    ]