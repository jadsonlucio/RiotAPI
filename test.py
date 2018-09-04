from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data,methods
from copy import deepcopy,copy

riotAPI = RiotAPI(["RGAPI-454ee132-826b-4662-b37a-e1b838229179", "RGAPI-f7dd612d-2704-4f6c-9407-1a682d590933"], "kr",
                  "pt_BR")

summoner = riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, batch_size=20,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets",verbose=20, queue=[420])


