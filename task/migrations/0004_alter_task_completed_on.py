# Generated by Django 5.1.1 on 2024-09-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_completed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
