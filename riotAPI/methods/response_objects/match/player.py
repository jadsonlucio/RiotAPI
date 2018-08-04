from .. import Response, Response_list

__all__ = ["Player", "Player_list"]


class Player(Response):
    """

    """

    def __init__(self, participantId, teamId, championId, spell1Id,
                 spell2Id, highestAchievedSeasonTier, stats, timeline, participantIdentitie):
        self.particiapantId = participantId
        self.teamId = teamId
        self.championId = championId
        self.spell1Id = spell1Id
        self.spell2Id = spell2Id
        self.highestAchievedSeasonTier = highestAchievedSeasonTier
        self.lane = timeline.pop("lane")
        self.role = timeline.pop("role")

        self.stats = Player_stats(stats)
        self.timeline = Player_timeline(timeline)

        self.currentPlatformId = None
        self.summonerName = None
        self.matchHistoryUri = None
        self.platformId = None
        self.currentAccountId = None
        self.profileIcon = None
        self.summonerId = None
        self.accountId = None

        super().__init__(**participantIdentitie)


class Player_list(Response_list):
    def load_response_object(self, kwargs):
        return Player(**kwargs)


class Player_stats(Response):
    def __init__(self, stats):
        super().__init__(**stats)


class Player_timeline(Response):
    def __init__(self, timeline):
        super().__init__(**timeline)
