from .. import Response_list
from . import Player_list

__all__ = ["Team", "Team_list"]


class Team(Player_list):
    def __init__(self, atributes_team, participants, participantIdentities):
        for key, value in zip(atributes_team.keys(), atributes_team.values()):
            self.__setattr__(key, value)

        for participant, participantIdentitie in zip(participants, participantIdentities):
            participant["participantIdentitie"] = participantIdentitie["player"]

        super().__init__(participants)


class Team_list(Response_list):
    def load_response_object(self, kwargs):
        return Team(**kwargs)
