def crawling_match_data(riotAPI, accountId, max_matchs, save=False, **filters):
    """
    Pega partidas

    :param riotAPI:
    :param accountId:
    :param max_matchs:
    :param save:
    :param filters:
    :return:
    """
    accountid_list = []
    match_list = []
    matchid_list = []

    accountid_list.append(accountId)
    accountid_list_index = 0

    while (len(match_list) < max_matchs):
        try:
            match_info_list = riotAPI.get_matchListByAccountId(accountid_list[accountid_list_index], **filters)
            for match_info in match_info_list:
                matchId = match_info.gameId
                if (matchId not in matchid_list):
                    match = riotAPI.get_matchById(matchId)
                    match_list.append(match)
                    matchid_list.append(matchId)

                    for accountId in match.accountId.ravel():
                        if (accountId not in accountid_list):
                            accountid_list.append(int(accountId))

                    print("Número de partidas coletadas:{0}".format(len(match_list)))
        except Exception as e:
            pass


        accountid_list_index = accountid_list_index + 1

    return matchid_list
