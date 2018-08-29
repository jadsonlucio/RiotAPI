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
        self.app_rate_limit = None
        self.app_rate_limit_count = None
        self.app_time_reset = None

        self.method_rate_limit = None
        self.method_rate_limit_count = None
        self.method_time_reset = None

        self.count_requests = None
        self.__blocked_api_keys = {}

        Requisition.__init__(self, response_data_type)

    def _add_blocked_api_key(self, api_key, type_block, seconds_blocked):
        """
        Adiciona uma api_key bloqueada ao __blocked_api_keys.

        :param api_key: api_key bloqueada.
        :param type_block: metodo block ou app block.
        :param seconds_blocked: tempo que a key vai permanecer bloqueada.
        :return: dict
        """

        dict = {"type_block": type_block,
                "seconds_blocked": seconds_blocked,
                "time_blocked": datetime.now(),
                "time_to_reset": datetime.now() + timedelta(seconds=self.method_time_reset)
                }

        self.__blocked_api_keys[api_key] = dict

        return dict

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
        headers_response = response.headers
        
        if ("X-Method-Rate-Limit" in headers_response):
            self.method_rate_limit, self.method_time_reset = [int(value) for value in
                                                              headers_response["X-Method-Rate-Limit"].split(":")]
            self.method_rate_limit_count = int(headers_response["X-Method-Rate-Limit-Count"].split(":")[0])

        if ("X-App-Rate-Limit" in headers_response):
            self.app_rate_limit, self.app_time_reset, self.app_rate_limit_count = [], [], []
            buckets_rate_limit = headers_response["X-App-Rate-Limit"].split(",")
            buckets_rate_limit_count = headers_response["X-App-Rate-Limit-Count"].split(",")
            for bucket_rate_limit, bucket_rate_limit_count in zip(buckets_rate_limit, buckets_rate_limit_count):
                app_rate_limit, app_time_reset =[int(value) for value in bucket_rate_limit.split(":")]
                app_rate_limit_count = int(bucket_rate_limit_count.split(":")[0])

                self.app_rate_limit.append(app_rate_limit)
                self.app_time_reset.append(app_time_reset)
                self.app_rate_limit_count.append(app_rate_limit_count)

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

        for app_rate_limit, app_rate_limit_count, app_time_reset in zip(self.app_rate_limit, self.app_rate_limit_count,
                                                                        self.app_time_reset):
            if (app_rate_limit_count == app_rate_limit - 1):
                dict = self._add_blocked_api_key(headers["X-Riot-Token"], "app", app_time_reset)
                raise MaxRequestAchieved(dict)

        if (self.method_rate_limit_count == self.method_rate_limit - 1):
            dict = self._add_blocked_api_key(headers["X-Riot-Token"], "method", self.method_time_reset)
            raise MaxRequestAchieved(dict)

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
