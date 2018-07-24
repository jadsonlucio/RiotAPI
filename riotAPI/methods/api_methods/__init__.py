from . import api_method
from .api_method import *
from . import match
from .match import *
from . import summoner
from .summoner import *

MatchById = MatchById()
MatchListByAccountId = MatchListByAccountId()
SummonerById = SummonerById()
SummonerByName = SummonerByName()
SummonerByAccountId = SummonerByAccountId()

__all__ = ["MatchById", "MatchListByAccountId", "SummonerById", "SummonerByName", "SummonerByAccountId"]
