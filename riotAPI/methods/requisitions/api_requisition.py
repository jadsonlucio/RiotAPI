from . import Requisition
from ...exceptions.max_requests import MaxRequestAchieved
from ...exceptions.response import is_invalid_request, get_invalid_request
from ...exceptions.response import is_server_error, get_server_error

from datetime import datetime, timedelta


class Requisition_API(Requisition):
    """
    Classe que representa uma requisição feita à api

    """

    def __init__(self, response_data_type):
        self.max_requests = None
        self.time_reset = None
        self.count_requests = None
        self.__blocked_api_keys = {}

        Requisition.__init__(self, response_data_type)

    def _verify_blocked_api_keys(self):
        """
        Vefica e remove as api_keys que não estão mais bloqueadas.

        :return: None
        """
        [self.__blocked_api_keys.pop(key) for key, value in self.__blocked_api_keys.items() if
         (value["time_to_reset"] >= datetime.now())]

    def _is_valid_response(self, response):
        """
        Faz uma validação da resposta recebida pela requisição à api, a fim de verificar
        se o codigo de resposta é valido e se a pagina retornou o json corretamente.

        :param response: objeto de resposta a uma requisição feita usando requests.get.
        :return: True or Exception.
        """

        status_code = response.status_code
        request = self.requests[-1]

        if (status_code == 200):
            self._process_valid_response(request, response)
            return True
        elif (is_invalid_request(status_code) or is_server_error(status_code)):
            self._process_invalid_response(request, response)
            return False

    def _process_valid_response(self, request, response):
        """
        Método que trata de uma resposta valida à requisição feita.

        :param request: dicionarios contendo os atributos passados para fazer a requisição
        :param response: objeto retornado atravez do metodo get contendo os dados de resposta a requisição.
        :return: None
        """

        headers = request["headers"]
        headers_response = response.headers

        self.max_requests, self.time_reset = [int(value) for value in
                                              headers_response["X-Method-Rate-Limit"].split(":")]

        self.count_requests = headers_response["X-Method-Rate-Limit-Count"].split(":")[0]

        if (self.count_requests == self.max_requests - 1):
            self.__blocked_api_keys[headers["X-Riot-Token"]] = {
                "seconds_blocked": self.time_reset,
                "time_blocked": datetime.now(),
                "time_to_reset": datetime.now() + timedelta(seconds=self.time_reset)
            }

            raise MaxRequestAchieved()

    def _process_invalid_response(self, request, response):
        """
        Método que trata de uma resposta invalida à requisição feita.

        :param request: dicionarios contendo os atributos passados para fazer a requisição
        :param response: objeto retornado atravez do metodo get contendo os dados de resposta a requisição.
        :return: None
        """

        url = request["url"]
        params = request["params"]
        headers = request["headers"]
        headers_response = response.headers
        status_code = response.status_code

        if (is_invalid_request(status_code)):
            RequestException = get_invalid_request(status_code)
            raise RequestException(url, headers, headers_response, params)
        elif (is_server_error(status_code)):
            RequestException = get_server_error(status_code)
            raise RequestException(url, headers, headers_response, params)
