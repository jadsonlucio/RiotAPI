from . import ResponseException

__all__ = ["InternalServerError", "ServiceUnavailable", "get_server_error",
           "is_server_error"]


class InternalServerError(ResponseException):
    """
    Classe que representa a exceção levantada por um erro interno do servidor.

    Codigo erro:500.

    """
    CODE = 500
    DESCRIPTION = "Esse erro indica uma condição ou exceção inesperada que impediu que o servidor cumprisse uma solicitação da API."

    COMMOM_REASONS = []


class ServiceUnavailable(ResponseException):
    """
    Classe que representa a exceção levantada por um erro causado pela indisponibilidade
    do servidor de manipular a solicitação devido a algum motivo.

    Cddigo erro:503.

    """

    CODE = 503
    DESCRIPTION = "Esse erro indica que o servidor está indisponível no momento para manipular solicitações devido a um motivo " \
                  "desconhecido. A resposta Serviço indisponível indica uma condição temporária que será aliviada após algum atraso."

    COMMOM_REASONS = []


def is_server_error(code):
    """
    Verifica se um codigo representa um erro do servidor.

    :param code: codigo de resposta do servidor.
    :return: boolean
    """
    for exception in __server_error_classes__:
        if (exception.CODE == code):
            return True

    return False


def get_server_error(code):
    """
    Retorna a classe do erro correspondente ao codigo passado se ele
    for ele for caracterizado como um erro do servidor, caso contrario
    vai ser lançado uma exeção.

    :param code:
    :return: codigo de resposta do servidor.
    """
    for exception in __server_error_classes__:
        if (exception.CODE == code):
            return exception

    raise Exception("code {0} not found as server error".format(code))


__server_error_classes__ = [InternalServerError, ServiceUnavailable]
