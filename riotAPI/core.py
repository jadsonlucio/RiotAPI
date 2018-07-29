from . import methods
from . import decorators
from . import extensions


class RiotAPI():
    """
    Classe principal da API, onde vão ser feitas todas as requisições
    tanto para a API quando para o ddragon.

    """

    def __init__(self, api_keys, region, language):
        """
        Inicializa um objeto to tipo RiotAPI.

        :param api_key: chave fornecida atravez da api da riot.
        :param region: região padrão em que vão ser feitas as buscas.
        :param language: linguagem padrão das requisições ao ddragon.
        """
        if (isinstance(api_keys, str)):
            api_keys = [api_keys]

        self.__api_keys = api_keys
        self.api_key_index = 0
        self.api_keys_size = len(self.__api_keys)

        self.region = region
        self.language = language

    # api_key
    @property
    def __api_key(self):
        return self.__api_keys[self.api_key_index]

    # Match methods

    @decorators.api_method
    def get_matchById(self, gameId, region=None):
        """

        :param gameId: Id da partida.
        :return: Match
        """

        return methods.MatchById.request(api_key=self.__api_key, region=region, gameId=gameId)

    @decorators.api_method
    def get_matchListByAccountId(self, accountId, beginIndex=None, endIndex=None,
                                 beginTime=None, endTime=None, queue=None, season=None, region=None):
        """

        :param accountId:
        :param beginIndex:
        :param endIndex:
        :param beginTime:
        :param endTime:
        :param queue:
        :param season:
        :return:
        """

        return methods.MatchListByAccountId.request(api_key=self.__api_key, region=region, accountId=accountId,
                                                    beginIndex=beginIndex, endIndex=endIndex, beginTime=beginTime,
                                                    endTime=endTime, queue=queue, season=season)

    # Summoner methods

    @decorators.api_method
    def get_summonerByAccountId(self, accountId, region=None):
        """

        :param accountId:
        :return: Summoner
        """

        return methods.SummonerByAccountId.request(api_key=self.__api_key, region=region, accountId=accountId)

    @decorators.api_method
    def get_summonerByName(self, summonerName, region=None):
        """

        :param summonerName:
        :return: Summoner
        """

        return methods.SummonerByName.request(api_key=self.__api_key, region=region, summonerName=summonerName)

    @decorators.api_method
    def get_summonerById(self, summonerId, region=None):
        """

        :param summonerId:
        :return: Summoner
        """

        return methods.SummonerById.request(api_key=self.__api_key, region=region, summonerId=summonerId)

    # ddragon methods

    @decorators.ddragon_method(language="pt_BR")
    def get_champions(self, patch_version=None, language=None):
        """

        :return: Champion_list
        """
        return methods.Champions.request(patch_version=patch_version, language=language)
