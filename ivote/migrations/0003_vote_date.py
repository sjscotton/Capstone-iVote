# Generated by Django 2.2.3 on 2019-07-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivote', '0002_auto_20190707_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_voter_id', models.CharField(default='00', max_length=15)),
                ('county_code', models.CharField(default='00', max_length=10)),
                ('election_date', models.CharField(default='00', max_length=15)),
            ],
        ),
    ]
