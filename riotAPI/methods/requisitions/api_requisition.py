from . import Requisition
from ...exceptions.response import is_invalid_request, get_invalid_request
from ...exceptions.response import is_server_error, get_server_error

class Requisition_API(Requisition):
    """
    Classe que representa uma requisição feita à api

    """

    def _is_valid_response(self, response):
        """
        Faz uma validação da resposta recebida pela requisição à api, a fim de verificar
        se o codigo de resposta é valido e se a pagina retornou o json corretamente.

        :param response: objeto de resposta a uma requisição feita usando requests.get.
        :return: True or Exception.
        """

        status_code = response.status_code
        headers_response = response.headers

        request=self.requests[-1]
        url=request["url"]
        params=request["params"]
        headers=request["headers"]

        if (status_code == 200):
            self.max_requests,self.time_reset=headers_response["X-Method-Rate-Limit"].split(":")
            self.count_requests=headers_response["X-Method-Rate-Limit-Count"].split(":")[0]
            return True
        elif (is_invalid_request(status_code)):
            RequestException = get_invalid_request(status_code)
            raise RequestException(url, headers, headers_response, params)
        elif (is_server_error(status_code)):
            RequestException = get_server_error(status_code)
            raise RequestException(url, headers, headers_response, params)
