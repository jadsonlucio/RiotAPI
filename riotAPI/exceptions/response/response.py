from datetime import datetime
from ...constants import FILE_LOG_PATH


class ResponseException(Exception):
    """
    Super-classe das exceções levantadas de acordo com a resposta do servidor.
    Mais informações em https://developer.riotgames.com/response-codes.html

    """
    CODE = None
    DESCRIPTION = None
    COMMOM_REASONS = None
    RESPONSE_LOG_PATH = FILE_LOG_PATH+"response_error.txt"

    def __init__(self, url_request, headers_request, headers_response, query_params):
        """
        Inicializa uma exceção

        :param url_request: url requisitada
        :param headers_request: cabeçalho embutido na requisição
        :param headers_response: cabeçalho de resposta do servidor
        :param query_params: parametros opcionais utilizados na requisição
        """
        self.url_request = url_request
        self.headers_request = headers_request
        self.headers_response = headers_response
        self.query_params = query_params

        self.save_log()

    def __str__(self):
        """
        Função responsavel por imprimir a mensagem de erro após a execeção ter sido
        lancada com o raise.

        :return: Str
        """
        error_msg = "Codigo de resposta do erro: {0}\n\nDescrição: {1}\n".format(self.CODE, self.DESCRIPTION)
        if (len(self.COMMOM_REASONS) > 0):
            error_msg = error_msg + "\nCausas comuns do erro:"
            for reason in self.COMMOM_REASONS:
                error_msg = error_msg + reason + "\n"
        return error_msg


    def save_log(self):
        """
        Salva em um arquivo de logs o tipo de erro de resposta a url utilizada para fazer a requisição
        os cabeçalhos de requisição e resposta e os parametros utilizados na requisição.

        :return: None
        """

        log_msg = "[{0}]\nCodigo do erro:{1}\nData da requisição:\nurl_requisitada:{2}\ncabecalho_requisitado:{3}\
                 \nparametros_requisitados:{4}\ncabecalho_resposta:{5}\n".format(str(datetime.now()), self.CODE, self.url_request,
                                                                                 self.headers_request,
                                                                                 self.query_params,
                                                                                 self.headers_response)

        file = open(self.RESPONSE_LOG_PATH, "a")
        file.writelines(log_msg)
