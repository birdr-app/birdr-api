# Generated by Django 4.2.3 on 2024-10-18 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdr', '0044_auto_20241018_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='player',
        ),
    ]
