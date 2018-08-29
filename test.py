from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data,methods
from copy import deepcopy,copy

riotAPI = RiotAPI(["RGAPI-e8c76c12-8f58-4ece-84f9-7220294c336e", "RGAPI-85022628-3107-4689-a378-63290d3b4e03"], "kr",
                  "pt_BR")

summoner = riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, save_after=1000,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets", queue=[420])


