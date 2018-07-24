from .. import Response, Response_list

from . import Player, Player_list
from . import Team_list

__all__ = ["Match", "Match_list"]


def get_participants_teams(teams, participants, participantIdentities):
    """
    Divide os participantes entre os times.

    [participants[cont:cont+size_teams] for cont in range(0,len(participants),size_teams)]

    :param teams:  Lista contendo estatisticas dos times.
    :param participants: Lista contendo estatisticas dos participantes da partida..
    :param participantIdentities: Lista contendo detalhes das contas dos participantes..
    :return: Lista contendo tuplas do time no formato (team_stats,participants_team,participantIdentities_team)
    """

    quant_teams = len(teams)
    size_team=int(len(participants)/quant_teams)
    teams_participants = [participants[cont:cont+size_team] for cont in range(0,len(participants),size_team)]
    teams_participantIdentities = [participantIdentities[cont:cont+size_team] for cont in range(0,len(participants),size_team)]

    teams = [
        {'atributes_team': atributes_team, 'participants': participants, 'participantIdentities': participantIdentities}
        for atributes_team, participants, participantIdentities in
        zip(teams, teams_participants, teams_participantIdentities)]

    return teams


class Match(Team_list):
    """
    Classe que representa o resultado do metodo getMatch, disponivel em
    https://developer.riotgames.com/api-methods/#match-v3/GET_getMatch

    """

    def __init__(self, gameId, platformId, gameCreation, gameDuration, queueId, mapId, seasonId,
                 gameVersion, gameMode, gameType, teams, participants, participantIdentities):
        """
        Inicializa um objeto do tipo Match.

        :param gameId: Id da partida.
        :param platformId: Id do servidor em que a partida foi jogada.
        :param gameCreation: Data em que a partida ocorreu em milesegundos.
        :param gameDuration: Duração da partida em segundos.
        :param queueId: codigo do tipo de partida.
        :param mapId: Id do map em que a partida foi jogada.
        :param seasonId: Id da temporada em que a partida ocorreu.
        :param gameVersion: versão do jogo.
        :param gameMode: Modo de jogo.
        :param gameType: Tipo de partida.
        :param teams: Lista contendo estatisticas dos times.
        :param participants: Lista contendo estatisticas dos participantes da partida.
        :param participantIdentities: Lista contendo detalhes das contas dos participantes.
        """

        self.gameId = gameId
        self.platformId = platformId
        self.gameCreation = gameCreation
        self.gameDuration = gameDuration
        self.queueId = queueId
        self.gameVersion = gameVersion
        self.gameMode = gameMode
        self.gameType = gameType

        self.map = mapId
        self.season = seasonId

        # self.teams=[Team(**kwargs_team) for kwargs_team in teams]
        teams = get_participants_teams(teams, participants, participantIdentities)
        super().__init__(teams)


class Match_list(Response_list):

    def load_response_object(self, kwargs):
        """
        Metodo que retorna um objeto do tipo Match

        :param kwargs: dicionario contendo as variaveis presentes na
        classe Match.
        :return: Match
        """

        return Match(**kwargs)
