# Generated by Django 3.1.5 on 2021-01-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
