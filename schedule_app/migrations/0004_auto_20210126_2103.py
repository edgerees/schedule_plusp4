# Generated by Django 3.1.5 on 2021-01-26 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0003_merge_20210126_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat_id',
            new_name='chatroom',
        ),
    ]