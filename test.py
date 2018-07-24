from riotAPI import RiotAPI

riotAPI=RiotAPI("ka","br1","pt_BR")
champions=riotAPI.get_champions(language="pt_BR")
