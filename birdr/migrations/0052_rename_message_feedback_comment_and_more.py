# Generated by Django 4.2.3 on 2024-11-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdr', '0051_feedback_countrychallenge_countrybadges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='score',
            new_name='rating',
        ),
    ]
