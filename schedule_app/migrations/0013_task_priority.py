# Generated by Django 3.1.5 on 2021-01-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0012_auto_20210121_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Not Important', 'Not Important'), ('Important', 'Important'), ('Very Important', 'Very Important')], max_length=200, null=True),
        ),
    ]
