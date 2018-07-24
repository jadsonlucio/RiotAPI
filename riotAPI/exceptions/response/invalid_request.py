from . import ResponseException

__all__ = ["BadRequest", "Forbidden", "Unauthoritzed", "NotFound",
           "RateLimitExceeded", "UnsupportedMediaType", "get_invalid_request",
           "is_invalid_request"]


class BadRequest(ResponseException):
    """
    Classe que representa a exceção levantada por um erro de sintaxe presente na url.

    Codigo erro:400.

    """

    CODE = 400
    DESCRIPTION = "Esse erro indica que há um erro de sintaxe na solicitação e, portanto, a solicitação foi negada." \
                  " O cliente não deve continuar a fazer solicitações semelhantes sem modificar a sintaxe ou as solicitações " \
                  "que estão sendo feitas."

    COMMOM_REASONS = [
        "Um parâmetro fornecido está no formato incorreto (por exemplo, uma string em vez de um inteiro).",
        "Um parâmetro fornecido é inválido (por exemplo, beginTime e startTime especificam um intervalo de tempo muito grande).",
        "Um parâmetro obrigatório não foi fornecido."]


class Unauthoritzed(ResponseException):
    """
    Classe que representa a exceção levantada pela falta de uma chave de autenticação na requisição.

    Codigo erro:401.

    """

    CODE = 401
    DESCRIPTION = "Esse erro indica que a solicitação sendo feita não continha as credenciais de autenticação necessárias (por exemplo, uma chave de API) e, " \
                  "portanto, foi negado o acesso ao cliente. O cliente não deve continuar a fazer solicitações semelhantes sem incluir uma chave de API na solicitação."

    COMMOM_REASONS = ["Uma chave de API não foi incluída na solicitação."]


class Forbidden(ResponseException):
    """
    Classe que representa a exceção levantada pela falta de uma chave de autenticação valida na requisição.

    Codigo erro:403.

    """

    CODE = 403
    DESCRIPTION = "Esse erro indica que o servidor entendeu a solicitação, mas se recusou a autorizá-la. Não há distinção entre um caminho inválido ou credenciais" \
                  "de autorização inválidas (por exemplo, uma chave de API). O cliente não deve continuar fazendo solicitações semelhantes"

    COMMOM_REASONS = ["Uma chave de API inválida foi fornecida com a solicitação da API.",
                      "Uma chave de API na lista negra foi fornecida com a solicitação da API.",
                      "A solicitação da API era para um caminho incorreto ou sem suporte."]


class NotFound(ResponseException):
    """
    Classe que representa a exceção levantada porque o servidor não conseguiu encontrar uma correspondência para a
    requisição feita.

    Codigo erro:404.

    """

    CODE = 404
    DESCRIPTION = "Esse erro indica que o servidor não encontrou uma correspondência para a solicitação da API que está sendo feita. " \
                  "Nenhuma indicação é dada se a condição é temporária ou permanente."

    COMMOM_REASONS = [
        "O ID ou nome fornecido não corresponde a nenhum recurso existente (por exemplo, não há invocador correspondente ao ID especificado).",
        "Não há recursos que correspondam aos parâmetros especificados."]


class UnsupportedMediaType(ResponseException):
    """
    Classe que representa a exceção levantada por uma definição incorreta do cabeçalho Content-Type.

    Codigo erro:415.

    """
    CODE = 415
    DESCRIPTION = "Esse erro indica que o servidor está se recusando a atender a solicitação porque o corpo da solicitação está em um formato que não é suportado."

    COMMOM_REASONS = ["O cabeçalho Content-Type não foi definido adequadamente."]


class RateLimitExceeded(ResponseException):
    """
    Classe que representa a exceção levantada porque se atingiu o limite de requisições feita a um metodo
    com uma api key.

    Codigo erro:429.

    """
    CODE = 429
    DESCRIPTION = "Esse erro indica que o aplicativo esgotou seu número máximo de chamadas de API permitidas por uma determinada duração." \
                  " Se o cliente receber uma resposta de Taxa Limite Excedida, o cliente deverá processar essa resposta e interromper " \
                  "futuras chamadas da API pela duração, em segundos, indicada pelo cabeçalho Retry-After. Aplicativos que violam esta " \
                  "política podem ter seu acesso desativado para preservar a integridade da API. Consulte a documentação de " \
                  "limitação de taxa,, em https://developer.riotgames.com/rate-limiting.html, para obter mais informações sobre como determinar se você tem uma taxa limitada e como evitá-la."

    COMMOM_REASONS = [
        "Chamadas de API não regulamentadas,ver o cabesalho de resposta e os logs de requisições para monitorar "
        "a atividade da sua chave API"]


def is_invalid_request(code):
    """
    Verifica se um codigo representa um erro de requisição.

    :param code: codigo de resposta do servidor.
    :return: boolean
    """
    for exception in __invalid_request_classes__:
        if (exception.CODE == code):
            return True

    return False


def get_invalid_request(code):
    """
    Retorna a classe do erro correspondente ao codigo passado se ele
    for ele for caracterizado como um erro do requisição, caso contrario
    vai ser lançado uma exeção.

    :param code: codigo do erro
    :return: codigo de resposta do servidor.
    """
    for exception in __invalid_request_classes__:
        if (exception.CODE == code):
            return exception

    raise Exception("code {0} not found as invalid request")


__invalid_request_classes__ = [BadRequest, NotFound, Forbidden, RateLimitExceeded,
                               UnsupportedMediaType, Unauthoritzed]
