from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data,methods
from copy import deepcopy,copy

riotAPI = RiotAPI(["RGAPI-1de1793c-2c82-4dc8-8840-8dfb0e8489a4", "RGAPI-f7dd612d-2704-4f6c-9407-1a682d590933"], "kr",
                  "pt_BR")

summoner = riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, save_after=100,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets",verbose=20, queue=[420],
                                 beginTime="20/8/2018")


