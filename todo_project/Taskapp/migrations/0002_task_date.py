# Generated by Django 4.2.11 on 2024-04-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-12-20'),
            preserve_default=False,
        ),
    ]
