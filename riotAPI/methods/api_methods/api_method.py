from .. import Requisition_API
from .. import Method



__all__ = ["API_Method"]


class API_Method(Method):
    """
    Super-classe dos metodos disponiveis na api, mais informações sobre eles
    em https://developer.riotgames.com/api-methods/

    """

    ROOT_URL = "https://{0}.api.riotgames.com/"
    RESPONSE_DATA_TYPE = "json"
    HEADERS_REQUEST = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }

    def __init__(self, version, base_url, custom_url, path_params, query_params, response_data_type="json"):
        """
        Inicializa um objeto do tipo API_Method

        :param version: versão atual do metodo dentro da api
        :param root_url: parte principal da url de requisicao que esta presente em todos os metodos no formato https://{regiao}.api.riotgames.com/
        :param base_url: parte da url de requisiçao que esta presente em todos os metodos de um modulo
        :param custom_url: parte custumizavel da url de requisiçao onde os parametros obrigatorios vão ser colocados,
        :param path_params: lista de dicionarios com a descrição dos atributos obrigatorios.
        :param query_params: lista de dicionarios com a descrição dos atributos opcionais.
        :param rate_limit: quantidade maxima de requisições permitidas
        """

        self.root_url = API_Method.ROOT_URL
        self.base_url = base_url
        self.custom_url = custom_url

        url = API_Method.ROOT_URL + base_url + version + custom_url
        requisition = Requisition_API(response_data_type)

        super().__init__(version, url, path_params, query_params, requisition)

    def _request(self, api_key, region, *path_params, **query_params):
        """
        Método responsavel por fazer uma requisição a api devolvendo um objeto da pagina
        de acordo com o response_data_type.

        :param api_key: key necessaria para realizar uma requisição na api.
        :param region: regiao aonde a requisiçao deve ser feita, mais sobre em https://google.com.
        :param path_params: parametos obrigatorios do metodo.
        :param query_params: parametos opcionais do metodo.
        :return: json
        """

        hearders = API_Method.HEADERS_REQUEST
        hearders["X-Riot-Token"] = api_key
        url = self.url.format(region,*path_params)

        if (self.path_attributes.validate(path_params) and self.query_attributes.validate(query_params)):
            return self.requisition(url, query_params, hearders)

