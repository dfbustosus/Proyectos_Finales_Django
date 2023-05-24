# Generated by Django 4.2.1 on 2023-05-17 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mensajeria", "0002_alter_messageschat_receiver_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chatroom",
            name="messages",
        ),
        migrations.AddField(
            model_name="messageschat",
            name="chat_room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="mensajeria.chatroom",
            ),
        ),
    ]
