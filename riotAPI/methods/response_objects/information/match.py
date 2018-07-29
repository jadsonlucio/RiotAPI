from .. import Response, Response_list

__all__ = ["Match_info", "Match_info_list"]


class Match_info(Response):
    """

    """
    def __init__(self, season, platformId, gameId, lane, timestamp, queue,
                 role, champion):
        """

        :param season:
        :param platformId:
        :param gameId:
        :param lane:
        :param timestamp:
        :param queue:
        :param role:
        :param champion:
        """

        self.season=season
        self.platformId=platformId
        self.gameId=gameId
        self.lane=lane
        self.timestamp=timestamp
        self.queue=queue
        self.role=role
        self.champion=champion

        super().__init__()

class Match_info_list(Response_list):
    def load_response_object(self, kwargs):
        return Match_info(**kwargs)

    def __init__(self, startIndex, endIndex, totalGames, matches):
        self.startIndex=startIndex
        self.endIndex=endIndex
        self.totalGames=totalGames

        super().__init__(matches)

