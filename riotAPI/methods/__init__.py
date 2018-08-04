from . import method
from .method import Method
from . import attribute


#requisitions
from . import requisitions
from .requisitions import *

# riotAPI methods
from . import api_methods
from .api_methods import *

# ddragon methods
from . import ddragon_methods
from .ddragon_methods import *

__ddragon_methods__ = ["Champions", "ChampionByName","ChampionSplashArt"]
__riotAPI_methods__ = ["SummonerById", "SummonerByName", "SummonerByAccountId", "MatchById",
                       "TimeLinesByMatchId","MatchListByAccountId"]

__all__ = __ddragon_methods__ + __riotAPI_methods__
