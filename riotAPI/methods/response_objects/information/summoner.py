from .. import Response, Response_list

__all__ = ["Summoner", "Summoner_list"]


class Summoner(Response):
    """
    classe que representa os resultados dos metodos do tipo
    getSummoner, disponiveis em https://developer.riotgames.com/api-methods/#summoner-v3

    """

    def __init__(self, id, accountId, name, profileIconId, revisionDate, summonerLevel):
        """
        Inicializa um objeto do tipo Summoner

        :param id: 	ID do jogador
        :param accountId: ID da conta
        :param name: Nome do jogador
        :param profileIconId: ID do icone de jogador associado com sua conta
        :param revisionDate: Data da ultima modificação nos dados do jogador em milesegundos. Os seguintes eventos
        vão atualizar esse parametro, mudança de icone, jogando tutorial ou tutorial avançado, finalisando uma partida
        mudando o nome do jogador.
        :param summonerLevel: Nivel do jogador associado a sua conta
        """
        self.id = id
        self.accountId = accountId
        self.name = name
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.summonerLevel = summonerLevel

        super().__init__()


class Summoner_list(Response_list):
    def load_response_object(self, kwargs):
        """
        Metodo que retorna um objeto to tipo Summoner.

        :param kwargs: dicionario contendo as variaveis presentes na
        classe Summoner.
        :return: Summoner
        """

        return Summoner(**kwargs)
