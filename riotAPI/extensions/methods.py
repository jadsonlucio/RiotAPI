def get_matchListByAccountId_v2(riotAPI, accountId, beginIndex=None, endIndex=None,
                                beginTime=None, endTime=None, queue=None, season=None, region=None):
    """
    Método get_matchListByAccountId modificado para functionar com mais
    de 100 partidas requisitadas.

    :param riotAPI: RiotAPI object
    :param accountId: id da conta do jogador.
    :param beginIndex: posição inicial na lista de jogos do jogador que as partidas vão se coletadas.
    :param endIndex: posição final na lista de jogos do jogador que as partidas vão se coletadas.
    :param beginTime: data(segundos) inicial em que as partidas vão se coletadas.
    :param endTime: data(segundos) final em que as partidas vão se coletadas.
    :param queue: lista contendo os ids dos tipos de partidas que vão ser coletadas.
    :param season: lista contendo od ids das temporadas permitidas para a coletagem de dados.
    :param region: região do servidor da requisição.
    :return: match_info_list
    """

    match_info_list = []

    filters={
        "beginIndex":beginIndex,"endIndex":endIndex,
        "beginTime":beginTime,"endTime":endTime,"queue":queue,
        "season":season,"region":region
    }

    if (beginIndex != None and endIndex != None):
        for cont in range(0, int((endIndex - beginIndex) / 100)):
            match_info_list = match_info_list + riotAPI.get_matchListByAccountId(accountId=accountId,**filters)

    return match_info_list+riotAPI.get_matchListByAccountId(accountId,**filters)