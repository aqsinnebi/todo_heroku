# Generated by Django 4.2.5 on 2023-10-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.DateTimeField(null=True),
        ),
    ]
