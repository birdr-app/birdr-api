# Generated by Django 4.2.3 on 2025-03-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdr', '0056_populate_challenge_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengelevel',
            name='tax_order',
            field=models.CharField(blank=True, help_text='Only show birds from this taxonomic order', max_length=200, null=True, verbose_name='Order'),
        ),
    ]
