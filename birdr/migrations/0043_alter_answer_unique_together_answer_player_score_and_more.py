# Generated by Django 4.2.3 on 2024-10-18 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birdr', '0042_auto_20241018_1711'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='answer',
            name='player_score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='.playerscore'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('player_score', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='playerscore',
            unique_together={('player', 'game')},
        ),
    ]
