# Generated by Django 3.1.5 on 2021-01-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0005_auto_20210120_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ManyToManyField(to='schedule_app.Position'),
        ),
    ]
