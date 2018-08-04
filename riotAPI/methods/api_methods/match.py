from . import API_Method
from ..response_objects import Match, Match_info_list

BASEURL = "lol/match/"
VERSION = "v3/"

__all__ = ["MatchById", "MatchListByAccountId","TimeLinesByMatchId"]


class MatchById(API_Method):
    """
    Classe responsavel por implementar o metodo getMatch representado pela url
    /lol/match/v3/matches/{matchId}

    """

    CUSTOM_URL = "matches/{1}"
    PATH_PARAMS = [{"name": "gameId", "description": "id da partida", "type": int}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(VERSION, BASEURL, MatchById.CUSTOM_URL,
                            MatchById.PATH_PARAMS, MatchById.QUERY_PARAMS)

    def request(self, api_key, region, gameId):
        """
        Método responsavel por fazer uma requisição
        por uma partida.

        :param gameId: id da partida.
        :return: Match
        """

        json = self._request(api_key, region, gameId)

        return Match(**json)


class MatchListByAccountId(API_Method):
    """
    Classe responsavel por implementar o metodo getMatch representado pela url
    /lol/match/v3/matches/{matchId}

    """

    CUSTOM_URL = "matchlists/by-account/{1}"
    PATH_PARAMS = [{"name": "accountId", "description": "id da conta do jogador", "type": int}]
    QUERY_PARAMS = [{"name": "endTime", "description": "", "type": int},
                    {"name": "beginIndex", "description": "", "type": int},
                    {"name": "beginTime", "description": "", "type": int},
                    {"name": "champion", "description": "", "type": list},
                    {"name": "endIndex", "description": "", "type": int},
                    {"name": "queue", "description": "", "type": list},
                    {"name": "season", "description": "", "type": list}]

    def __init__(self):
        super().__init__(VERSION, BASEURL, MatchListByAccountId.CUSTOM_URL,
                            MatchListByAccountId.PATH_PARAMS, MatchListByAccountId.QUERY_PARAMS)

    def request(self, api_key, region, accountId, beginIndex=None, endIndex=None,
                beginTime=None, endTime=None, queue=None, season=None):
        """
        Método responsavel por fazer uma requisição
        por uma lista de partidas.

        :param accountId: id da conta do jogador.
        :return: Match_list
        """

        json = self._request(api_key, region, accountId, beginIndex=beginIndex, endIndex=endIndex,
                             beginTime=beginTime, endTime=endTime, queue=queue, season=season)

        return Match_info_list(**json)


class TimeLinesByMatchId(API_Method):
    """
    Classe responsavel por implementar o metodo timelines representado pela url
    /lol/match/v3/timelines/by-match/{matchId}.

    obs:Uma timeline é uma serie de eventos que aconteceram durante o jogo, que são
    marcados de acordo com o seu tempo.

    """

    CUSTOM_URL = "timelines/by-match/{1}"
    PATH_PARAMS = [{"name": "gameId", "description": "id da partida", "type": int}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(VERSION, BASEURL, TimeLinesByMatchId.CUSTOM_URL,
                         TimeLinesByMatchId.PATH_PARAMS, TimeLinesByMatchId.QUERY_PARAMS)

    def request(self, api_key, region, gameId):
        """
        Método responsavel por fazer uma requisição
        por uma timeline de uma partida.

        :param gameId: id da partida.
        :return: dict
        """

        print("entrou")
        json = self._request(api_key, region, gameId)

        return json