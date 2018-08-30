from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data,methods
from copy import deepcopy,copy

riotAPI = RiotAPI(["RGAPI-a49f8e78-d5ec-47c6-915b-8acf8670cf14", "RGAPI-f7dd612d-2704-4f6c-9407-1a682d590933"], "kr",
                  "pt_BR")

summoner = riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, save_after=100,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets",verbose=20, queue=[420])


