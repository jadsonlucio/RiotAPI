class AttributeTypeError(Exception):
    """
    Classe que representa a excessão levantada quando o tipo de um
    atributo passado a um metodo não corresponde ao tipo real do atributo
    na api.

    """

    def __init__(self, passed_type, attribute):
        """
        Inicializa uma excessão do tipo AttributeTypeError

        :param passed_attribute_type : tipo do atributo fornecido.
        :param attribute: atributo.
        """

        self.attribute = attribute
        self.passed_type = passed_type

    def __str__(self):
        """
        Função responsavel por imprimir a mensagem de erro após a execeção ter sido
        lancada com o raise.

        :return: Str
        """
        error_msg = "O atributo {0} foi fornecido com o tipo {1}, mas o tipo correto é {2}\n Descrição do atributo: {3}".format(
            self.attribute.name, self.passed_type, self.attribute.type, self.attribute.description
        )

        return error_msg


class AttributeNameError(Exception):
    """
    Classe que representa a excessão levantada quando o nome de um
    atributo opcional não corresponde a nenhum dos atributos opcionais
    do metodo

    """

    def __init__(self, attribute_name, query_attributes):
        """
        Inicializa uma excessão do tipo AttributeNameError

        :param attribute_name: nome do atributo passado.
        :param query_attributes: lista de atributos opcionais do metodo
        """

        self.attribute_name = attribute_name
        self.query_attributes = query_attributes

    def __str__(self):
        """
        Função responsavel por imprimir a mensagem de erro após a execeção ter sido
        lancada com o raise.

        :return: Str
        """
        error_msg = "O atributo {0} não existe nesse metodo\n Lista dos atributos opcionais desse metodo: ".format(
            self.attribute_name
        )
        for attribute in self.query_attributes:
            error_msg = error_msg + attribute.name

        return error_msg


class AttributeSizeError(Exception):
    """
    Classe que representa a excessão levantada quando a quantidade
    de atributos obrigatorios passados difere da quantidade de atributos
    obrigatorios do metodo

    """

    def __init__(self, passed_path_params, path_attributes):
        """
        Inicializa  uma excessão do tipo AttributeSizeError

        :param passed_path_params: lista dos atributos obrigatorios passados.
        :param path_attributes: lista dos atributos obrigatorios.
        """
        self.passed_path_params = passed_path_params
        self.path_attributes = path_attributes

    def __str__(self):
        """
        Função responsavel por imprimir a mensagem de erro após a execeção ter sido
        lancada com o raise.

        :return: Str
        """
        error_msg = "A quantidade de atributos obrigatorios passados foi de {0}\n Lista de atributos obrigatorios desse metodo: ".format(
            len(self.passed_path_params))

        for attribute in self.path_attributes:
            error_msg = error_msg + "\nNome atributo: {0}, tipo: {1}".format(attribute.name, attribute.type)

        return error_msg
