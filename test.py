import mysql.connector as mariadb
import rg_api_key
import requests
import json
import asyncio




connection = mariadb.connect(user='root', password='123321Almitimo', database='RiotGames')

cursor = connection.cursor()

#Create Table in MySQL DB=====================================================================

tb_create_summoner = """CREATE TABLE Summoner_V4
				(id Varchar(255), accountId Varchar(255), puuid Varchar(255),
					name Varchar(255), profileIconId INT, revisionDate BIGINT, summonerLevel INT)"""

tb_create_matchlist = """CREATE TABLE MatchList_V4
				(accountId Varchar(255), platformId Varchar(255), gameId BIGINT, champion INT,
					queue INT, season INT, timestamp BIGINT, role Varchar(255), lane Varchar(255))"""



tb_create_matchTeamData = """CREATE TABLE MatchTeam_V4
				(gameId BIGINT, platformId Varchar(255), gameCreation BIGINT, gameDuration INT, queueId INT,
					mapId INT, seasonId INT, gameVersion Varchar(255), gameMode Varchar(255), gameType Varchar(255),
					teamId INT, win Varchar(255), firstBlood BOOLEAN, firstTower BOOLEAN, firstInhibitor BOOLEAN,
					firstBaron BOOLEAN, firstDragon BOOLEAN, firstRiftHerald BOOLEAN, towerKills INT, inhibitorKills INT,
					baronKills INT, dragonKills INT, vilemawKills INT, riftHeraldKills INT, dominionVictoryScore INT)"""

tb_create_matchParticipantData = """CREATE TABLE MatchParticipant_V4
				(gameId BIGINT, platformId Varchar(255), gameCreation BIGINT, gameDuration INT, queueId INT,
					mapId INT, seasonId INT, gameVersion Varchar(255), gameMode Varchar(255), gameType Varchar(255),
					teamId INT, participantId INT, accountId Varchar(255), summonerName Varchar(255), summonerId Varchar(255),
					matchHistoryUri Varchar(255), championId INT, spell1Id INT, spell2Id INT, role Varchar(255),
					lane Varchar(255), win BOOLEAN, item0 INT, item1 INT, item2 INT, item3 INT, item4 INT, item5 INT,
					item6 INT, kills INT, deaths INT, assists INT, largestKillingSpree INT, largestMultiKill INT,
					killingSprees INT, longestTimeSpentLiving INT, doubleKills INT, tripleKills INT, quadraKills INT,
					pentaKills INT, unrealKills INT, totalDamageDealt INT, magicDamageDealt INT, physicalDamageDealt INT,
					trueDamageDealt INT, largestCriticalStrike INT, totalDamageDealtToChampions INT, magicDamageDealtToChampions INT,
					physicalDamageDealtToChampions INT, trueDamageDealtToChampions INT, totalHeal INT, totalUnitsHealed INT,
					damageSelfMitigated INT, damageDealtToObjectives INT, damageDealtToTurrets INT, visionScore INT, 
					timeCCingOthers INT, totalDamageTaken INT, magicalDamageTaken INT, physicalDamageTaken INT, 
					trueDamageTaken INT, goldEarned INT, goldSpent INT, turretKills INT, inhibitorKills INT,
					totalMinionsKilled INT, neutralMinionsKilled INT, neutralMinionsKilledTeamJungle INT,
					neutralMinionsKilledEnemyJungle INT, totalTimeCrowdControlDealt INT, champLevel INT,
					visionWardsBoughtInGame INT, sightWardsBoughtInGame INT, wardsPlaced INT, wardsKilled INT,
					firstBloodKill BOOLEAN, firstBloodAssist BOOLEAN, firstTowerKill BOOLEAN, firstTowerAssist BOOLEAN,
					firstInhibitorKill BOOLEAN, firstInhibitorAssist BOOLEAN)"""


# Execute Table Creation

# cursor.execute(tb_create_summoner)
# cursor.execute(tb_create_matchlist)
# cursor.execute(tb_create_matchTeamData)
# cursor.execute(tb_create_matchParticipantData)



# connection.commit()

#End of Creation, this above can be commented out===================================================

async def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(summonerName) + "?api_key=" + APIKey
    #print(URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    # Here I return the JSON we just got.
    return response.json()

async def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(ID) + "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()

async def requestMatchList(region, accountId, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + str(accountId) + "?api_key=" + APIKey

    response = requests.get(URL)
    return response.json()

def getMatchId(responseJSON3, matchNumber):
    
    return matchId['matches'][matchNumber]['gameId']

async def requestMatchInfo(region, matchId, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + str(matchId) + "?api_key=" + APIKey

    response = requests.get(URL)
    return response.json()


#API key, summoner input, localization
region = "EUW1"

APIKey = rg_api_key.riot_api_key

#This is where the actual code starts===========================================================================
async def main():
	#Import Summoner Data-------------------------------------------------------------------------------------
	summonerName = input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: ')
	summonerData = await requestSummonerData(region, summonerName, APIKey)

	#catching Error if it is API related, it will pop up with first call of responseJSON
	try:
		id				= summonerData['id']
	except KeyError:
		print("API related Error")
		exit()

	accountId 		= summonerData['accountId']
	puuid 			= summonerData['puuid']
	name 			= summonerData['name']
	profileIconId 	= summonerData['profileIconId']
	revisionDate	= summonerData['revisionDate']
	summonerLevel	= summonerData['summonerLevel']

	#Insert imported SummonerData to SQL Database
	# cursor.execute("""INSERT INTO Summoner_V4
	# 					(id , accountId , puuid , name , profileIconId , revisionDate , summonerLevel)
	# 					VALUES (%s,%s,%s,%s,%s,%s,%s)""",
	# 					(id , accountId , puuid , name , profileIconId , revisionDate , summonerLevel))

	# connection.commit()

	#Import matchList Data---------------------------------------------------------------------------------

	responseJSONMatchList = await requestMatchList(region, summonerData['accountId'], APIKey)

	#get a number of matchIDs of the matchlist JSON and put the matchIDs into a list
	matchIdList = []

	#Only Update DB with new MatchList entries
	#query the DB for newest existing entry and save the table
	getDBPlayerMatchList = """SELECT * FROM MatchList_V4 WHERE accountId = """ + "'" +str(accountId) + "'" + """ GROUP BY gameId
						ORDER BY `MatchList_V4`.`timestamp`  DESC"""

	cursor.execute(getDBPlayerMatchList)

	DBPlayerMatchList = cursor.fetchall()

	#Check from newest to oldest matches from Riotservers if they exist in newest DB entry
	for i in range(len(responseJSONMatchList['matches'])):

		try:
			if responseJSONMatchList['matches'][i]['gameId'] == DBPlayerMatchList[0][2]:
				print(responseJSONMatchList['matches'][i]['gameId'], " was last new matchId to be imported.")
				break

			else:

				matchIdList.append(responseJSONMatchList['matches'][i]['gameId'])
					
				print("Importing matchId ", responseJSONMatchList['matches'][i]['gameId'])

				platformId 		= responseJSONMatchList['matches'][i]['platformId']
				gameId 			= responseJSONMatchList['matches'][i]['gameId']
				champion 		= responseJSONMatchList['matches'][i]['champion']
				queue 			= responseJSONMatchList['matches'][i]['queue']
				season 			= responseJSONMatchList['matches'][i]['season']
				timestamp 		= responseJSONMatchList['matches'][i]['timestamp']
				role 			= responseJSONMatchList['matches'][i]['role']
				lane 			= responseJSONMatchList['matches'][i]['lane']

				#Insert imported responseJSONMatchList to SQL Database
				cursor.execute("""INSERT INTO MatchList_V4
									(accountId, platformId , gameId , champion , queue , season , timestamp , role, lane)
									VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
									(accountId, platformId , gameId , champion , queue , season , timestamp , role, lane))

				connection.commit()

		except IndexError:

			matchIdList.append(responseJSONMatchList['matches'][i]['gameId'])
				
			print("Importing matchId ", responseJSONMatchList['matches'][i]['gameId'])

			platformId 		= responseJSONMatchList['matches'][i]['platformId']
			gameId 			= responseJSONMatchList['matches'][i]['gameId']
			champion 		= responseJSONMatchList['matches'][i]['champion']
			queue 			= responseJSONMatchList['matches'][i]['queue']
			season 			= responseJSONMatchList['matches'][i]['season']
			timestamp 		= responseJSONMatchList['matches'][i]['timestamp']
			role 			= responseJSONMatchList['matches'][i]['role']
			lane 			= responseJSONMatchList['matches'][i]['lane']

			#Insert imported responseJSONMatchList to SQL Database
			cursor.execute("""INSERT INTO MatchList_V4
								(accountId, platformId , gameId , champion , queue , season , timestamp , role, lane)
								VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
								(accountId, platformId , gameId , champion , queue , season , timestamp , role, lane))

			connection.commit()


	#Import match Team Data---------------------------------------------------------------------------------

	# For all matches in matchList, get Data
	# Exit programm if this players data is up to date
	if len(matchIdList) ==0:
		print("DB is up to date.")
		exit()

	y = int(input("Start importing at which number 0-99? "))
	for k in range(y,len(matchIdList)):

		matchInfoData = await requestMatchInfo(region, matchIdList[k], APIKey)
		print("Importing "+str(matchIdList[k])+ " ("+ str((k+1))+ "/"+ str(len(matchIdList))+")")

		# General Game Data
		gameId 					= matchInfoData['gameId']
		platformId 				= matchInfoData['platformId']
		gameCreation 			= matchInfoData['gameCreation']
		gameDuration 			= matchInfoData['gameDuration']
		queueId 				= matchInfoData['queueId']
		mapId 					= matchInfoData['mapId']
		seasonId 				= matchInfoData['seasonId']
		gameVersion 			= matchInfoData['gameVersion']
		gameMode 				= matchInfoData['gameMode']
		gameType 				= matchInfoData['gameType']

		#Split into Team Data
		for i in range(2):
			teamId 					= matchInfoData['teams'][i]['teamId']
			win 					= matchInfoData['teams'][i]['win']
			firstBlood 				= matchInfoData['teams'][i]['firstBlood']
			firstTower 				= matchInfoData['teams'][i]['firstTower']
			firstInhibitor 			= matchInfoData['teams'][i]['firstInhibitor']
			firstBaron 				= matchInfoData['teams'][i]['firstBaron']
			firstDragon 			= matchInfoData['teams'][i]['firstDragon']
			firstRiftHerald 		= matchInfoData['teams'][i]['firstRiftHerald']
			towerKills 				= matchInfoData['teams'][i]['towerKills']
			inhibitorKills 			= matchInfoData['teams'][i]['inhibitorKills']
			baronKills 				= matchInfoData['teams'][i]['baronKills']
			dragonKills 			= matchInfoData['teams'][i]['dragonKills']
			vilemawKills 			= matchInfoData['teams'][i]['vilemawKills']
			riftHeraldKills 		= matchInfoData['teams'][i]['riftHeraldKills']
			dominionVictoryScore 	= matchInfoData['teams'][i]['dominionVictoryScore']

			#Insert imported matchTeamData to SQL Database
			cursor.execute("""INSERT INTO MatchTeam_V4
								(gameId, platformId, gameCreation, gameDuration, queueId, mapId, seasonId,
								gameVersion, gameMode, gameType, teamId, win, firstBlood, firstTower,
								firstInhibitor, firstBaron, firstDragon, firstRiftHerald, towerKills,
								inhibitorKills, baronKills, dragonKills, vilemawKills, riftHeraldKills, dominionVictoryScore)
								VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
								(gameId, platformId, gameCreation, gameDuration, queueId, mapId, seasonId,
								gameVersion, gameMode, gameType, teamId, win, firstBlood, firstTower,
								firstInhibitor, firstBaron, firstDragon, firstRiftHerald, towerKills,
								inhibitorKills, baronKills, dragonKills, vilemawKills, riftHeraldKills, dominionVictoryScore))

			connection.commit()
			print("Team",i+1, "import Done")

		#Now Matches
		for player in range(len(matchInfoData['participants'])):

			gameId 					= matchInfoData['gameId']
			platformId 				= matchInfoData['platformId']
			gameCreation 			= matchInfoData['gameCreation']
			gameDuration 			= matchInfoData['gameDuration']
			queueId 				= matchInfoData['queueId']
			mapId 					= matchInfoData['mapId']
			seasonId 				= matchInfoData['seasonId']
			gameVersion 			= matchInfoData['gameVersion']
			gameMode 				= matchInfoData['gameMode']
			gameType 				= matchInfoData['gameType']
			
			teamId 			= matchInfoData['participants'][player]['teamId']
			participantId 	= matchInfoData['participants'][player]['participantId']
			accountId		= matchInfoData['participantIdentities'][player]['player']['accountId']
			summonerName 	= matchInfoData['participantIdentities'][player]['player']['summonerName']
			
			matchHistoryUri = matchInfoData['participantIdentities'][player]['player']['matchHistoryUri']
			championId 		= matchInfoData['participants'][player]['championId']
			spell1Id 		= matchInfoData['participants'][player]['spell1Id']
			spell2Id 		= matchInfoData['participants'][player]['spell2Id']
			role 			= matchInfoData['participants'][player]['timeline']['role']
			lane 			= matchInfoData['participants'][player]['timeline']['lane']

			win 								= matchInfoData['participants'][player]['stats']['win']
			item0 								= matchInfoData['participants'][player]['stats']['item0']
			item1 								= matchInfoData['participants'][player]['stats']['item1']
			item2 								= matchInfoData['participants'][player]['stats']['item2']
			item3 								= matchInfoData['participants'][player]['stats']['item3']
			item4 								= matchInfoData['participants'][player]['stats']['item4']
			item5 								= matchInfoData['participants'][player]['stats']['item5']
			item6 								= matchInfoData['participants'][player]['stats']['item6']
			kills 								= matchInfoData['participants'][player]['stats']['kills']
			deaths 								= matchInfoData['participants'][player]['stats']['deaths']
			assists 							= matchInfoData['participants'][player]['stats']['assists']
			largestKillingSpree 				= matchInfoData['participants'][player]['stats']['largestKillingSpree']
			largestMultiKill 					= matchInfoData['participants'][player]['stats']['largestMultiKill']
			killingSprees 						= matchInfoData['participants'][player]['stats']['killingSprees']
			longestTimeSpentLiving 				= matchInfoData['participants'][player]['stats']['longestTimeSpentLiving']
			doubleKills 						= matchInfoData['participants'][player]['stats']['doubleKills']
			tripleKills 						= matchInfoData['participants'][player]['stats']['tripleKills']
			quadraKills 						= matchInfoData['participants'][player]['stats']['quadraKills']
			pentaKills 							= matchInfoData['participants'][player]['stats']['pentaKills']
			unrealKills 						= matchInfoData['participants'][player]['stats']['unrealKills']
			totalDamageDealt 					= matchInfoData['participants'][player]['stats']['totalDamageDealt']
			magicDamageDealt 					= matchInfoData['participants'][player]['stats']['magicDamageDealt']
			physicalDamageDealt 				= matchInfoData['participants'][player]['stats']['physicalDamageDealt']
			trueDamageDealt 					= matchInfoData['participants'][player]['stats']['trueDamageDealt']
			largestCriticalStrike 				= matchInfoData['participants'][player]['stats']['largestCriticalStrike']
			totalDamageDealtToChampions 		= matchInfoData['participants'][player]['stats']['totalDamageDealtToChampions']
			magicDamageDealtToChampions 		= matchInfoData['participants'][player]['stats']['magicDamageDealtToChampions']
			physicalDamageDealtToChampions 		= matchInfoData['participants'][player]['stats']['physicalDamageDealtToChampions']
			trueDamageDealtToChampions 			= matchInfoData['participants'][player]['stats']['trueDamageDealtToChampions']
			totalHeal 							= matchInfoData['participants'][player]['stats']['totalHeal']
			totalUnitsHealed 					= matchInfoData['participants'][player]['stats']['totalUnitsHealed']
			damageSelfMitigated 				= matchInfoData['participants'][player]['stats']['damageSelfMitigated']
			damageDealtToObjectives 			= matchInfoData['participants'][player]['stats']['damageDealtToObjectives']
			damageDealtToTurrets 				= matchInfoData['participants'][player]['stats']['damageDealtToTurrets']
			visionScore 						= matchInfoData['participants'][player]['stats']['visionScore']
			timeCCingOthers 					= matchInfoData['participants'][player]['stats']['timeCCingOthers']
			totalDamageTaken 					= matchInfoData['participants'][player]['stats']['totalDamageTaken']
			magicalDamageTaken 					= matchInfoData['participants'][player]['stats']['magicalDamageTaken']
			physicalDamageTaken 				= matchInfoData['participants'][player]['stats']['physicalDamageTaken']
			trueDamageTaken 					= matchInfoData['participants'][player]['stats']['trueDamageTaken']
			goldEarned 							= matchInfoData['participants'][player]['stats']['goldEarned']
			goldSpent 							= matchInfoData['participants'][player]['stats']['goldSpent']
			turretKills 						= matchInfoData['participants'][player]['stats']['turretKills']
			inhibitorKills 						= matchInfoData['participants'][player]['stats']['inhibitorKills']
			totalMinionsKilled 					= matchInfoData['participants'][player]['stats']['totalMinionsKilled']
			neutralMinionsKilled 				= matchInfoData['participants'][player]['stats']['neutralMinionsKilled']
			
			totalTimeCrowdControlDealt 			= matchInfoData['participants'][player]['stats']['totalTimeCrowdControlDealt']
			champLevel 							= matchInfoData['participants'][player]['stats']['champLevel']
			visionWardsBoughtInGame 			= matchInfoData['participants'][player]['stats']['visionWardsBoughtInGame']
			sightWardsBoughtInGame 				= matchInfoData['participants'][player]['stats']['sightWardsBoughtInGame']
			

			try:
				firstInhibitorKill 					= matchInfoData['participants'][player]['stats']['firstInhibitorKill']
				firstInhibitorAssist 				= matchInfoData['participants'][player]['stats']['firstInhibitorAssist']
				neutralMinionsKilledTeamJungle 		= matchInfoData['participants'][player]['stats']['neutralMinionsKilledTeamJungle']
				neutralMinionsKilledEnemyJungle 	= matchInfoData['participants'][player]['stats']['neutralMinionsKilledEnemyJungle']
				wardsPlaced 						= matchInfoData['participants'][player]['stats']['wardsPlaced']
				wardsKilled 						= matchInfoData['participants'][player]['stats']['wardsKilled']
				summonerId 							= matchInfoData['participantIdentities'][player]['player']['summonerId']
				firstTowerKill 						= matchInfoData['participants'][player]['stats']['firstTowerKill']
				firstTowerAssist 					= matchInfoData['participants'][player]['stats']['firstTowerAssist']
				firstBloodKill 						= matchInfoData['participants'][player]['stats']['firstBloodKill']
				firstBloodAssist 					= matchInfoData['participants'][player]['stats']['firstBloodAssist']
			except KeyError:
				firstInhibitorKill 					= False
				firstInhibitorAssist 				= False
				neutralMinionsKilledTeamJungle 		= 0
				neutralMinionsKilledEnemyJungle 	= 0
				wardsPlaced 						= 0
				wardsKilled 						= 0
				summonerId 							= ""
				firstTowerKill 						= False
				firstTowerAssist 					= False
				firstBloodKill 						= False
				firstBloodAssist 					= False

			#Insert imported matchParticipant Data to SQL Database
			cursor.execute("""INSERT INTO MatchParticipant_V4
								(gameId, platformId, gameCreation, gameDuration, queueId, mapId, seasonId, gameVersion,
								gameMode, gameType, teamId, participantId, accountId, summonerName, summonerId,
								matchHistoryUri, championId, spell1Id, spell2Id, role, lane, win, item0, item1,
								item2, item3, item4, item5, item6, kills, deaths, assists, largestKillingSpree, largestMultiKill,
								killingSprees, longestTimeSpentLiving, doubleKills, tripleKills, quadraKills, pentaKills,
								unrealKills, totalDamageDealt, magicDamageDealt, physicalDamageDealt, trueDamageDealt,
								largestCriticalStrike, totalDamageDealtToChampions, magicDamageDealtToChampions,
								physicalDamageDealtToChampions, trueDamageDealtToChampions, totalHeal, totalUnitsHealed,
								damageSelfMitigated, damageDealtToObjectives, damageDealtToTurrets, visionScore,
								timeCCingOthers, totalDamageTaken, magicalDamageTaken, physicalDamageTaken, trueDamageTaken,
								goldEarned, goldSpent, turretKills, inhibitorKills, totalMinionsKilled, neutralMinionsKilled,
								neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle, totalTimeCrowdControlDealt,
								champLevel, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, wardsKilled, firstBloodKill,
								firstBloodAssist, firstTowerKill, firstTowerAssist, firstInhibitorKill, firstInhibitorAssist)
								VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
								%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
								%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
								(gameId, platformId, gameCreation, gameDuration, queueId, mapId, seasonId, gameVersion,
								gameMode, gameType, teamId, participantId, accountId, summonerName, summonerId,
								matchHistoryUri, championId, spell1Id, spell2Id, role, lane, win, item0, item1,
								item2, item3, item4, item5, item6, kills, deaths, assists, largestKillingSpree, largestMultiKill,
								killingSprees, longestTimeSpentLiving, doubleKills, tripleKills, quadraKills, pentaKills,
								unrealKills, totalDamageDealt, magicDamageDealt, physicalDamageDealt, trueDamageDealt,
								largestCriticalStrike, totalDamageDealtToChampions, magicDamageDealtToChampions,
								physicalDamageDealtToChampions, trueDamageDealtToChampions, totalHeal, totalUnitsHealed,
								damageSelfMitigated, damageDealtToObjectives, damageDealtToTurrets, visionScore,
								timeCCingOthers, totalDamageTaken, magicalDamageTaken, physicalDamageTaken, trueDamageTaken,
								goldEarned, goldSpent, turretKills, inhibitorKills, totalMinionsKilled, neutralMinionsKilled,
								neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle, totalTimeCrowdControlDealt,
								champLevel, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, wardsKilled, firstBloodKill,
								firstBloodAssist, firstTowerKill, firstTowerAssist, firstInhibitorKill, firstInhibitorAssist))

			connection.commit()
		print("Match Data Import Done")




loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(main())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
