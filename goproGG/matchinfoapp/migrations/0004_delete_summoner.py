# Generated by Django 3.0.5 on 2020-04-20 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchinfoapp', '0003_matchlistv4_matchparticipantv4_matchteamv4_summonerv4'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Summoner',
        ),
    ]
