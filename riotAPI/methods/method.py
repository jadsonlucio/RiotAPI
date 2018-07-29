from colorama import Fore
from .attribute import Query_atributes, Path_atributes


class Method():
    """
    Super-classe que define os methodos abstratos de um
    metodo.

    """
    __INSTANCE = None
    ROOT_URL = None
    CUSTOM_URL = None
    RESPONSE_DATA_TYPE = None
    HEADERS_REQUEST = None

    PATH_PARAMS = None
    QUERY_PARAMS = None

    def __init__(self, version, url, path_params, query_params, requisition):
        """

        :param url: url completa da requisição.
        :param version: versão do metodo na api ou do jogo no ddragon.
        :param response_data_type: tipo de dado
        :param path_params: parametros obrigatorios passado atravez da url de requisição.
        :param query_params: parametros opcionais.
        """

        self.url = url
        self.version = version

        self.path_attributes = Path_atributes(path_params)
        self.query_attributes = Query_atributes(query_params)

        self.requisition = requisition

    def request(self, *args, **kwargs):
        """
        Metodo abstrato responsavel por fazer a requisição e devolver
        um objeto de acordo com o método requisitad.

        :param args:
        :param kwargs:
        :return Object: Objeto que representa o metodo requisitado.
        """
        raise NotImplementedError

    def _request(self, *path_params, **query_params):
        """
        Metodo abstrato responsavel por fazer a requisição a url do metodo
        e retorna um objeto que tem o tipo de acordo com response_data_type.

        :param path_params: parametros obrigatorios do metodo.
        :param kwargs: parametros opcionais do metodo.
        :return: Object
        """

        raise NotImplementedError

    def __new__(cls, *args, **kwargs):
        """
        Implementação do padrão singleton em python.

        :param args:
        :param kwargs:
        :return: Singleton instance of Method
        """

        if (cls.__INSTANCE == None):
            cls.__INSTANCE = object.__new__(cls)

        return cls.__INSTANCE

    def __str__(self):
        string = self.__class__.__name__ + "("

        for name, type in zip(self.path_attributes.names, self.path_attributes.types):
            string = string + "{0}{1}:{2}{3}, ".format(Fore.RED, name, type.__name__, Fore.RESET)

        for name, type in zip(self.query_attributes.names, self.query_attributes.types):
            string = string + "{0}{1}:{2}{3}, ".format(Fore.BLUE, name, type.__name__, Fore.RESET)

        string = string[:-2] + ")"

        return string
