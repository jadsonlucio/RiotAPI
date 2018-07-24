from .. import Response, Response_list

__all__ = ["Champion", "Champion_list"]


class Champion(Response):
    """
    Class que representa o resultado do metodo ChampionByName.

    """

    def __init__(self, version, stats, name, title, image, tags, partype,
                 key, id, blurb, info, enemytips=None, skins=None, passive=None,
                 recommended=None, allytips=None, lore=None, spells=None):
        """
        Inicializa um objeto do tipo Champion

        :param version: versão do jogo em que os dados do campeão foi coletado.
        :param enemytips: Dicas para se jogar contra annie.
        :param stats: status base do campeão.
        :param name: Nome do campeão.
        :param title: Titulo do campeão.
        :param image: Imagem do campeão.
        :param tags: Classe e subclasse do campeão(Mago,Tank,Atirador,..).
        :param partype:
        :param skins: Lista das skins do campeão.
        :param passive: Dicionario com a descriação e a imagem da passiva do campeão.
        :param recommended: Lista de itens recomendados para o campeão.
        :param allytips: Dicas para se jogar com o campeão.
        :param key: id do campeão.
        :param lore: Historia do campeão.
        :param id: Nome do campeão
        :param blurb:
        :param spells: Lista de feitiços do campeão.
        :param info: Pontuações do campeão nos quesitos de attack,defense,magic e difficulty.
        """

        self.enemytips = enemytips
        self.name = name
        self.title = title
        self.classes = tags
        self.partype = partype
        self.skins = skins
        self.passive = passive
        self.recommended = recommended
        self.allytips = allytips
        self.key = key
        self.lore = lore
        self.id = id
        self.blurb = blurb
        self.spells = spells
        self.info = info

        self.stats = Champion_stats(stats)

        super().__init__()


class Champion_stats(Response):
    def __init__(self, stats):
        super().__init__(**stats)


class Champion_list(Response_list):
    def load_response_object(self, kwargs):
        return Champion(**kwargs)
