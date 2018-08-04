from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data,methods
from copy import deepcopy,copy

riotAPI = RiotAPI(["RGAPI-a2d40974-2826-48f7-ab0e-cfd35f62312c", "RGAPI-85022628-3107-4689-a378-63290d3b4e03"], "kr",
                  "pt_BR")

champions = riotAPI.get_champions()
print(champions.dict[0].keys())

"""
crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, save_after=1000,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets", queue=[420])
"""
