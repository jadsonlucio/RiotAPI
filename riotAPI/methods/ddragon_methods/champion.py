from . import Ddragon_Method
from ..response_objects import Champion, Champion_list

__all__ = ["Champions","ChampionSplashArt"]


class Champions(Ddragon_Method):
    """
    Classe responsavel por implementar o metodo que pega
    a lista de todos os campeões do jogo.

    """

    CUSTOM_URL = "cdn/{0}/data/{1}/champion.json"
    RESPONSE_DATA_TYPE = "json"

    PATH_PARAMS = [{"name": "patch_version", "description": "versão do jogo", "type": str},
                   {"name": "language", "description": "linguagem dos dados rotornados", "type": str}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(Champions.CUSTOM_URL, Champions.RESPONSE_DATA_TYPE,
                         Champions.PATH_PARAMS, Champions.QUERY_PARAMS)

    def request(self, patch_version=None, language=None):
        """
        :return: Champion_list
        """

        if (patch_version == None):
            patch_version = self.version

        json = self._request(patch_version, language)

        return Champion_list(json["data"])


class ChampionById():
    pass


class ChampionSplashArt(Ddragon_Method):
    """
    Classe responsavel por implementar o metodo que pega
    a imagem de um campeão do jogo.

    """

    CUSTOM_URL = "cdn/img/champion/splash/{0}"
    RESPONSE_DATA_TYPE = "image"

    PATH_PARAMS = [{"name": "champion_splash_name", "description": "name of sprite image", "type": str}]
    QUERY_PARAMS = []

    def __init__(self):
        super().__init__(ChampionSplashArt.CUSTOM_URL, ChampionSplashArt.RESPONSE_DATA_TYPE,
                         ChampionSplashArt.PATH_PARAMS, ChampionSplashArt.QUERY_PARAMS)


    def request(self, image_name):
        """
        :return: PIL Image
        """

        image = self._request(image_name)

        return image