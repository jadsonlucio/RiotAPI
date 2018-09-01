import os 
import json
import pandas as pd

from .methods import get_matchListByAccountId_v2
from ..exceptions.response import NotFound
from ..constants import FILE_PATH

MAX_MATCHS_PLAYER = 200


def crawling_match_data(riotAPI, accountId, max_matchs, save=True, save_after=1000, save_path="", 
                        verbose=False, elo="gold", **filters):
    """
    Pega partidas de varios jogadores diferentes.

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

    region = riotAPI.region
    cache_path = FILE_PATH+"cache/extensions/{0}_{1}.json".format(region,elo)

    if os.path.isfile(cache_path):
        with open(cache_path,"r") as fp:
            loaded_dict = json.load(fp)
            accountid_list = loaded_dict["accountid_list"]
            accountid_list_index = loaded_dict["accountid_list_index"]
            matchid_list = loaded_dict["matchid_list"]
            batch_index = loaded_dict["batch_index"]
            

        os.remove(cache_path)

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
                        save_cache(cache_path, accountid_list,accountid_list_index, 
                                   matchid_list, batch_index)
                        save_matchlist_batch(save_path, save_after, match_list, batch_index)
                        batch_index = batch_index + 1

                if len(matchid_list) >= max_matchs:
                    break
                if(verbose and len(matchid_list)%verbose == 0):
                    print("Número de partidas coletadas:{0}".format(len(matchid_list)))

        except NotFound as e:
            pass
        except Exception as e:
            print(str(e))
            save_cache(cache_path, accountid_list,accountid_list_index, 
                       matchid_list, batch_index)
            continue



        accountid_list_index = accountid_list_index + 1

    return match_list


def save_cache(cache_path ,accountid_list, accountid_list_index, matchid_list, batch_index):
    dict_to_save = {
        "accountid_list":accountid_list,
        "accountid_list_index":accountid_list_index,
        "matchid_list":matchid_list,
        "batch_index":batch_index
    }

    with open(cache_path,"w+") as fp:
        json.dump(dict_to_save, fp)


def save_matchlist_batch(save_path, save_after, match_list , batch_index):
    match_list_dataframes = [match.dataframe for match in match_list[batch_index * save_after:]]
    match_list_dataframe = pd.concat(match_list_dataframes, ignore_index=True)
    match_list_dataframe.to_csv("{0}/dataframe_{1}.csv".format(save_path, batch_index), index=False,
                                index_label=False)