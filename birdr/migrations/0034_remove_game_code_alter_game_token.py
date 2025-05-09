# Generated by Django 4.2.3 on 2024-10-14 15:15

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('birdr', '0033_game_media_game_repeat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='code',
        ),
        migrations.AlterField(
            model_name='game',
            name='token',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=8, max_length=10, prefix=''),
        ),
    ]
