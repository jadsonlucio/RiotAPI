from .constants import PATCH_LAST_VERSION
from .. import Requisition_Ddragon
from .. import Method
from ...libs import isfile,read_file,create_file,set_abs_path


__all__ = ["Ddragon_Method"]


class Ddragon_Method(Method):
    ROOT_URL = "http://ddragon.leagueoflegends.com/"
    HEADERS_REQUEST = {
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }

    def __init__(self, base_url, response_data_type, path_params, query_params, version=None):
        """

        :param base_url: url base do metodo
        :param response_data_type: tipo do objeto retornado por _request
        :param path_params: atributos obrigatorios para requisão ao metodo.
        :param query_params: atributos opcionais para requisão ao metodo.
        :param version: versão do patch. caso não difinido a versão sera a ultima do jogo.
        :param rate_limit: quantidade de requisições máximas.
        """

        self.root_url = Ddragon_Method.ROOT_URL
        self.base_url = base_url

        if (version == None):
            version = PATCH_LAST_VERSION

        url = self.root_url + self.base_url
        requisition=Requisition_Ddragon(response_data_type)

        super().__init__(version, url, path_params, query_params, requisition)

    def _request(self, *path_params):
        """
        Método responsavel por fazer uma requisição ao ddragon devolvendo um objeto da pagina
        de acordo com o response_data_type.

        :param path_params: parametos obrigatorios do metodo.
        :return:
        """

        url = self.url.format(*path_params)
        headers = Ddragon_Method.HEADERS_REQUEST
        path = "files/cache/ddragon/"+url.replace(self.root_url,"")
        path = set_abs_path(path)

        if(isfile(path)):
            data=read_file(path,self.requisition.response_data_type)
        elif(self.path_attributes.validate(path_params)):
            data = self.requisition(url, hearders=headers)
            create_file(path,data,self.requisition.response_data_type)

        return data


