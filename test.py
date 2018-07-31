from riotAPI import RiotAPI
from riotAPI.extensions import crawling_match_data

riotAPI = RiotAPI(["RGAPI-dbfc6142-65c0-4dc5-9ceb-68d79c59891d", "RGAPI-85022628-3107-4689-a378-63290d3b4e03"], "br1",
                  "pt_BR")
summoner = riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI, summoner.accountId, 50000, save=True, save_after=1000,
                                 save_path=r"C:/Users/pandaQ/Documents/datasets", queue=[420])