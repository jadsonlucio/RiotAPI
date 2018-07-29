import requests
from PIL import Image
from io import BytesIO
from time import ctime

__all__ = ["Requisition"]
MAX_ATTEMPTS = 20


class Requisition():
    """
    Classe responsavel por gerenciar todas as requisições feitas
    por um metodo.

    """

    def __init__(self, response_data_type):
        self.__response_data_type = response_data_type
        self.requests = []

    def __call__(self, url, params={}, hearders={}):
        """
        Faz uma requisição a uma pagina e retorna um objeto de acordo
        com o data_type requerido.

        :param url: url da requisição.
        :param hearders: cabecalhos da requisição.
        :param params: parametros opcionais da requisição.
        :param data_type: tipo de dado retornado.
        :return:

        """

        self.requests.append({"url": url, "params": params, "headers": hearders, "time": ctime()})
        if (self.__response_data_type == "json"):
            return self.__request_json(url, params, hearders)
        elif (self.__response_data_type == "image"):
            return self.__request_image(url, params, hearders)
        else:
            raise Exception("request data type {0} doesn'n exist".format(self.__response_data_type))

    def get(self, url, params, headers, count_attempts=0):
        """
        Método que faz uma requisição do tipo get a uma url.

        :param url: url de requisição.
        :param params: parametros passados pelo metodo get.
        :param headers: cabeçalho de requisição.
        :param count_attempts: quantidade de tentaticas da requisição.
        :return: Response
        """

        if (count_attempts < MAX_ATTEMPTS):
            try:
                request = requests.get(url, params, headers=headers)
                return request
            except requests.exceptions.ConnectionError as e:
                count_attempts = count_attempts + 1
                return self.get(url, params, headers, count_attempts)
        else:
            raise Exception(
                "O maximo de tentativas de requisição foi atingido, por favor verique sua conexão com a internet")

    def __request_json(self, url, params, headers):
        """
        Faz uma requisição atravez do metodo get com o auxilio da biblioteca requests
        e retorna o json contido na pagina caso não ocorra nenhum erro.

        :return: dicionario que contem o json retornado pelo servidor.
        """

        response = self.get(url, params, headers=headers)
        if (self._is_valid_response(response)):
            return response.json()

    def __request_image(self, url, params, headers):
        """
        Faz uma requisição atravez do metodo get com o auxilio da biblioteca requests
        e retorna a imagem contida na pagina caso não ocorra nenhum erro.

        :return: PIL Image
        """

        response = self.get(url, params, headers=headers)
        if (self._is_valid_response(response)):
            return Image.open(BytesIO(response.content))



    def _is_valid_response(self, response):
        """
        Metodo abstrato que verifica se o objeto de resposta recebido pelo
        metodo requests.get é valido para o retorno.

        :param response: Objeto de resposta retornado pelo metodo requests.get
        :return: boolean
        """
        raise NotImplementedError


    @property
    def response_data_type(self):
        return self.__response_data_type

    @response_data_type.getter
    def response_data_type(self):
        return self.__response_data_type
