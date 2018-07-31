from . import Requisition

__all__=["Requisition_Ddragon"]

class Requisition_Ddragon(Requisition):
    """
    Classe que representa uma requisição feita ao servidor
    ddragon

    """

    def _is_valid_response(self, response):
        """

        :param response: objeto de resposta a uma requisição feita usando requests.get.
        :return: True or Exception.
        """

        status_code = response.status_code

        if (status_code == 200):
            return True


    def _process_invalid_response(self,request, response):
        pass

    def _process_valid_response(self, request, response):
        pass