from . import API_Method
from ..response_objects import Summoner

BASE_URL = "lol/summoner/"
VERSION = "v3/"

__all__ = ["SummonerById", "SummonerByName", "SummonerByAccountId"]


class SummonerByAccountId(API_Method):
    """
    Classe responsavel por implementar o metodo getByAccountId representado pela url
    /lol/summoner/v3/summoners/by-account/{accountId}

    """

    CUSTOM_URL = "summoners/by-account/{1}"
    PATH_PARAMS = [{"name": "accountId", "description": "id da conta do jogador", "type": int}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(VERSION, BASE_URL, SummonerByAccountId.CUSTOM_URL,
                            SummonerByAccountId.PATH_PARAMS, SummonerByAccountId.QUERY_PARAMS)

    def request(self, api_key, region, accountId):
        """
        Método responsavel por fazer uma requisição
        por um summoner.

        :param accountId: id da conta do jogador.
        :return: Summoner
        """

        json = self._request(api_key, region, accountId)

        return Summoner(**json)


class SummonerByName(API_Method):
    """
    Classe responsavel por implementar o metodo getBySummonerName representado pela url
    /lol/summoner/v3/summoners/by-name/{summonerName}


    """

    CUSTOM_URL = "summoners/by-name/{1}"
    PATH_PARAMS = [{"name": "summonerName", "description": r"nick da conta do jogador", "type": str}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(VERSION, BASE_URL, SummonerByName.CUSTOM_URL,
                            SummonerByName.PATH_PARAMS, SummonerByName.QUERY_PARAMS)

    def request(self, api_key, region, summonerName):
        """
        Método responsavel por fazer uma requisição
        por um summoner.

        :param summonerName: nick da conta do jogador.
        :return: Summoner
        """

        json = self._request(api_key, region, summonerName)

        return Summoner(**json)


class SummonerById(API_Method):
    """
    Classe responsavel por implementar o metodo getBySummonerId representado pela url
    /lol/summoner/v3/summoners/{summonerId}

    """

    CUSTOM_URL = "summoners/{1}"
    PATH_PARAMS = [{"name": "summonerId", "description": "id do jogador", "type": int}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(VERSION, BASE_URL, SummonerById.CUSTOM_URL,
                            SummonerById.PATH_PARAMS, SummonerById.QUERY_PARAMS)

    def request(self, api_key, region, summonerId):
        """
        Método responsavel por fazer uma requisição
        por um summoner.

        :param summonerId: id do jogador.
        :return: Summoner
        """

        json = self._request(api_key, region, summonerId)

        return Summoner(**json)
