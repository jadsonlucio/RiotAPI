from riotAPI import RiotAPI
from riotAPI.methods import MatchListByAccountId
from riotAPI.extensions import crawling_match_data


riotAPI=RiotAPI("RGAPI-2f9596b4-6173-4925-95c8-5f73d0777eac","br1","pt_BR")
summoner=riotAPI.get_summonerByName("kami")

crawling_match_data(riotAPI,summoner.accountId,500)