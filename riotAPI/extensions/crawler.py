import pandas as pd

from .methods import get_matchListByAccountId_v2
from ..exceptions.response import NotFound

MAX_MATCHS_PLAYER = 200


def crawling_match_data(riotAPI, accountId, max_matchs, save=True, save_after=1000, save_path="", **filters):
    """
    Pega partidas de verios jogadores diferentes.

    :param riotAPI: RiotAPI object
    :param accountId: id da conta do jogador que vai ser utilizado para pegar as informações dos outros jogadores
    :param max_matchs: numero maximo de partidas coletadas antes de parar
    :param save: salvar os dados apos um erro.
    :param save_after: valor que define a quantidade minima de partidas capturadas para o salvamento.
    :param save_path: local onde os arquivos vão ser salvos.
    :param filters: filtros de partida como por exemplo campeões.
    :return: lista de partidas coletadas.
    """
    accountid_list = []
    match_list = []
    matchid_list = []
    batch_index = 0

    accountid_list.append(accountId)
    accountid_list_index = 0

    while (len(match_list) < max_matchs):
        try:
            match_info_list = get_matchListByAccountId_v2(riotAPI, accountid_list[accountid_list_index], **filters)

            for match_info in match_info_list:
                matchId = match_info.gameId
                if (matchId not in matchid_list):
                    match = riotAPI.get_matchById(matchId)
                    match_list.append(match)
                    matchid_list.append(matchId)

                    for accountId in match.accountId.ravel():
                        if (accountId not in accountid_list):
                            accountid_list.append(int(accountId))

                    if (save and len(match_list) % save_after == 0):
                        match_list_dataframes = [match.dataframe for match in
                                                 match_list[batch_index * save_after:(batch_index + 1) * save_after]]
                        match_list_dataframe = pd.concat(match_list_dataframes, ignore_index=True)
                        match_list_dataframe.to_csv("{0}/dataframe_{1}.csv".format(save_path, batch_index), index=False,
                                                    index_label=False)
                        batch_index = batch_index + 1

                if (len(match_list) >= max_matchs):
                    break

                print("Número de partidas coletadas:{0}".format(len(matchid_list)))
        except NotFound as e:
            pass
        except Exception as e:
            print(str(e))

        accountid_list_index = accountid_list_index + 1

    return match_list
