# Generated by Django 3.1.5 on 2021-01-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0013_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_due',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
