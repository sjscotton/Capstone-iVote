# Generated by Django 2.2.3 on 2019-07-10 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivote', '0006_county_votes_zero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='county_votes',
            name='max_votes',
        ),
    ]
