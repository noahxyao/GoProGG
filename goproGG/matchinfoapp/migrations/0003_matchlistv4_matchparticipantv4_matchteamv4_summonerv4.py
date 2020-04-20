# Generated by Django 3.0.5 on 2020-04-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchinfoapp', '0002_auto_20200418_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchlistV4',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False)),
                ('accountid', models.CharField(blank=True, db_column='accountId', max_length=255, null=True)),
                ('platformid', models.CharField(blank=True, db_column='platformId', max_length=255, null=True)),
                ('gameid', models.BigIntegerField(blank=True, db_column='gameId', null=True)),
                ('champion', models.IntegerField(blank=True, null=True)),
                ('queue', models.IntegerField(blank=True, null=True)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('lane', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'MatchList_V4',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MatchparticipantV4',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False)),
                ('gameid', models.BigIntegerField(blank=True, db_column='gameId', null=True)),
                ('platformid', models.CharField(blank=True, db_column='platformId', max_length=255, null=True)),
                ('gamecreation', models.BigIntegerField(blank=True, db_column='gameCreation', null=True)),
                ('gameduration', models.IntegerField(blank=True, db_column='gameDuration', null=True)),
                ('queueid', models.IntegerField(blank=True, db_column='queueId', null=True)),
                ('mapid', models.IntegerField(blank=True, db_column='mapId', null=True)),
                ('seasonid', models.IntegerField(blank=True, db_column='seasonId', null=True)),
                ('gameversion', models.CharField(blank=True, db_column='gameVersion', max_length=255, null=True)),
                ('gamemode', models.CharField(blank=True, db_column='gameMode', max_length=255, null=True)),
                ('gametype', models.CharField(blank=True, db_column='gameType', max_length=255, null=True)),
                ('teamid', models.IntegerField(blank=True, db_column='teamId', null=True)),
                ('participantid', models.IntegerField(blank=True, db_column='participantId', null=True)),
                ('accountid', models.CharField(blank=True, db_column='accountId', max_length=255, null=True)),
                ('summonername', models.CharField(blank=True, db_column='summonerName', max_length=255, null=True)),
                ('summonerid', models.CharField(blank=True, db_column='summonerId', max_length=255, null=True)),
                ('matchhistoryuri', models.CharField(blank=True, db_column='matchHistoryUri', max_length=255, null=True)),
                ('championid', models.IntegerField(blank=True, db_column='championId', null=True)),
                ('spell1id', models.IntegerField(blank=True, db_column='spell1Id', null=True)),
                ('spell2id', models.IntegerField(blank=True, db_column='spell2Id', null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('lane', models.CharField(blank=True, max_length=255, null=True)),
                ('win', models.IntegerField(blank=True, null=True)),
                ('item0', models.IntegerField(blank=True, null=True)),
                ('item1', models.IntegerField(blank=True, null=True)),
                ('item2', models.IntegerField(blank=True, null=True)),
                ('item3', models.IntegerField(blank=True, null=True)),
                ('item4', models.IntegerField(blank=True, null=True)),
                ('item5', models.IntegerField(blank=True, null=True)),
                ('item6', models.IntegerField(blank=True, null=True)),
                ('kills', models.IntegerField(blank=True, null=True)),
                ('deaths', models.IntegerField(blank=True, null=True)),
                ('assists', models.IntegerField(blank=True, null=True)),
                ('largestkillingspree', models.IntegerField(blank=True, db_column='largestKillingSpree', null=True)),
                ('largestmultikill', models.IntegerField(blank=True, db_column='largestMultiKill', null=True)),
                ('killingsprees', models.IntegerField(blank=True, db_column='killingSprees', null=True)),
                ('longesttimespentliving', models.IntegerField(blank=True, db_column='longestTimeSpentLiving', null=True)),
                ('doublekills', models.IntegerField(blank=True, db_column='doubleKills', null=True)),
                ('triplekills', models.IntegerField(blank=True, db_column='tripleKills', null=True)),
                ('quadrakills', models.IntegerField(blank=True, db_column='quadraKills', null=True)),
                ('pentakills', models.IntegerField(blank=True, db_column='pentaKills', null=True)),
                ('unrealkills', models.IntegerField(blank=True, db_column='unrealKills', null=True)),
                ('totaldamagedealt', models.IntegerField(blank=True, db_column='totalDamageDealt', null=True)),
                ('magicdamagedealt', models.IntegerField(blank=True, db_column='magicDamageDealt', null=True)),
                ('physicaldamagedealt', models.IntegerField(blank=True, db_column='physicalDamageDealt', null=True)),
                ('truedamagedealt', models.IntegerField(blank=True, db_column='trueDamageDealt', null=True)),
                ('largestcriticalstrike', models.IntegerField(blank=True, db_column='largestCriticalStrike', null=True)),
                ('totaldamagedealttochampions', models.IntegerField(blank=True, db_column='totalDamageDealtToChampions', null=True)),
                ('magicdamagedealttochampions', models.IntegerField(blank=True, db_column='magicDamageDealtToChampions', null=True)),
                ('physicaldamagedealttochampions', models.IntegerField(blank=True, db_column='physicalDamageDealtToChampions', null=True)),
                ('truedamagedealttochampions', models.IntegerField(blank=True, db_column='trueDamageDealtToChampions', null=True)),
                ('totalheal', models.IntegerField(blank=True, db_column='totalHeal', null=True)),
                ('totalunitshealed', models.IntegerField(blank=True, db_column='totalUnitsHealed', null=True)),
                ('damageselfmitigated', models.IntegerField(blank=True, db_column='damageSelfMitigated', null=True)),
                ('damagedealttoobjectives', models.IntegerField(blank=True, db_column='damageDealtToObjectives', null=True)),
                ('damagedealttoturrets', models.IntegerField(blank=True, db_column='damageDealtToTurrets', null=True)),
                ('visionscore', models.IntegerField(blank=True, db_column='visionScore', null=True)),
                ('timeccingothers', models.IntegerField(blank=True, db_column='timeCCingOthers', null=True)),
                ('totaldamagetaken', models.IntegerField(blank=True, db_column='totalDamageTaken', null=True)),
                ('magicaldamagetaken', models.IntegerField(blank=True, db_column='magicalDamageTaken', null=True)),
                ('physicaldamagetaken', models.IntegerField(blank=True, db_column='physicalDamageTaken', null=True)),
                ('truedamagetaken', models.IntegerField(blank=True, db_column='trueDamageTaken', null=True)),
                ('goldearned', models.IntegerField(blank=True, db_column='goldEarned', null=True)),
                ('goldspent', models.IntegerField(blank=True, db_column='goldSpent', null=True)),
                ('turretkills', models.IntegerField(blank=True, db_column='turretKills', null=True)),
                ('inhibitorkills', models.IntegerField(blank=True, db_column='inhibitorKills', null=True)),
                ('totalminionskilled', models.IntegerField(blank=True, db_column='totalMinionsKilled', null=True)),
                ('neutralminionskilled', models.IntegerField(blank=True, db_column='neutralMinionsKilled', null=True)),
                ('neutralminionskilledteamjungle', models.IntegerField(blank=True, db_column='neutralMinionsKilledTeamJungle', null=True)),
                ('neutralminionskilledenemyjungle', models.IntegerField(blank=True, db_column='neutralMinionsKilledEnemyJungle', null=True)),
                ('totaltimecrowdcontroldealt', models.IntegerField(blank=True, db_column='totalTimeCrowdControlDealt', null=True)),
                ('champlevel', models.IntegerField(blank=True, db_column='champLevel', null=True)),
                ('visionwardsboughtingame', models.IntegerField(blank=True, db_column='visionWardsBoughtInGame', null=True)),
                ('sightwardsboughtingame', models.IntegerField(blank=True, db_column='sightWardsBoughtInGame', null=True)),
                ('wardsplaced', models.IntegerField(blank=True, db_column='wardsPlaced', null=True)),
                ('wardskilled', models.IntegerField(blank=True, db_column='wardsKilled', null=True)),
                ('firstbloodkill', models.IntegerField(blank=True, db_column='firstBloodKill', null=True)),
                ('firstbloodassist', models.IntegerField(blank=True, db_column='firstBloodAssist', null=True)),
                ('firsttowerkill', models.IntegerField(blank=True, db_column='firstTowerKill', null=True)),
                ('firsttowerassist', models.IntegerField(blank=True, db_column='firstTowerAssist', null=True)),
                ('firstinhibitorkill', models.IntegerField(blank=True, db_column='firstInhibitorKill', null=True)),
                ('firstinhibitorassist', models.IntegerField(blank=True, db_column='firstInhibitorAssist', null=True)),
            ],
            options={
                'db_table': 'MatchParticipant_V4',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MatchteamV4',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False)),
                ('gameid', models.BigIntegerField(blank=True, db_column='gameId', null=True)),
                ('platformid', models.CharField(blank=True, db_column='platformId', max_length=255, null=True)),
                ('gamecreation', models.BigIntegerField(blank=True, db_column='gameCreation', null=True)),
                ('gameduration', models.IntegerField(blank=True, db_column='gameDuration', null=True)),
                ('queueid', models.IntegerField(blank=True, db_column='queueId', null=True)),
                ('mapid', models.IntegerField(blank=True, db_column='mapId', null=True)),
                ('seasonid', models.IntegerField(blank=True, db_column='seasonId', null=True)),
                ('gameversion', models.CharField(blank=True, db_column='gameVersion', max_length=255, null=True)),
                ('gamemode', models.CharField(blank=True, db_column='gameMode', max_length=255, null=True)),
                ('gametype', models.CharField(blank=True, db_column='gameType', max_length=255, null=True)),
                ('teamid', models.IntegerField(blank=True, db_column='teamId', null=True)),
                ('win', models.CharField(blank=True, max_length=255, null=True)),
                ('firstblood', models.IntegerField(blank=True, db_column='firstBlood', null=True)),
                ('firsttower', models.IntegerField(blank=True, db_column='firstTower', null=True)),
                ('firstinhibitor', models.IntegerField(blank=True, db_column='firstInhibitor', null=True)),
                ('firstbaron', models.IntegerField(blank=True, db_column='firstBaron', null=True)),
                ('firstdragon', models.IntegerField(blank=True, db_column='firstDragon', null=True)),
                ('firstriftherald', models.IntegerField(blank=True, db_column='firstRiftHerald', null=True)),
                ('towerkills', models.IntegerField(blank=True, db_column='towerKills', null=True)),
                ('inhibitorkills', models.IntegerField(blank=True, db_column='inhibitorKills', null=True)),
                ('baronkills', models.IntegerField(blank=True, db_column='baronKills', null=True)),
                ('dragonkills', models.IntegerField(blank=True, db_column='dragonKills', null=True)),
                ('vilemawkills', models.IntegerField(blank=True, db_column='vilemawKills', null=True)),
                ('riftheraldkills', models.IntegerField(blank=True, db_column='riftHeraldKills', null=True)),
                ('dominionvictoryscore', models.IntegerField(blank=True, db_column='dominionVictoryScore', null=True)),
            ],
            options={
                'db_table': 'MatchTeam_V4',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SummonerV4',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=255, null=True)),
                ('accountid', models.CharField(blank=True, db_column='accountId', max_length=255, null=True)),
                ('puuid', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('profileiconid', models.IntegerField(blank=True, db_column='profileIconId', null=True)),
                ('revisiondate', models.BigIntegerField(blank=True, db_column='revisionDate', null=True)),
                ('summonerlevel', models.IntegerField(blank=True, db_column='summonerLevel', null=True)),
            ],
            options={
                'db_table': 'Summoner_V4',
                'managed': True,
            },
        ),
    ]