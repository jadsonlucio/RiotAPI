from ..exceptions import AttributeTypeError, AttributeNameError, AttributeSizeError

__all__ = ["Path_atributes", "Query_atributes"]


class Attribute():
    """
    Classe dos atributos passados através da url de uma requisição a api.

    """

    def __init__(self, type, name, description):
        """
        Inicializa um objeto do tipo Attribute.

        :param type: tipo da atributo
        :param name: nome do atributo
        :param description: descrição do atributo
        """
        self.type = type
        self.name = name
        self.description = description

    def __eq__(self, other):
        """
        metodo que verifica se um atributo e igual a outro.

        :param other: Attribute object
        :return: True or False
        """
        if (isinstance(other, Attribute)):
            if (self.name == other.name and self.type == other.type):
                return True
        elif (isinstance(other, tuple) or isinstance(other, list)):
            if (self.name == other[0] and self.type == other[1]):
                return True
        else:
            if (type(other) == self.type):
                return True

        return False

    def __str__(self):
        return "Nome atributo:{0}\nTipo:{1}\nDescrição:{2}".format(self.name,
                                                                   self.type, self.description)


class Atrribute_list(list):
    """
    classe que representa uma lista de atributos para a requisição
    a um metodo, sejam eles de path ou de query.

    """

    def __init__(self, list_params):
        list.__init__(self)

        for parametro in list_params:
            self.append(Attribute(**parametro))

    def validate(self, *args, **kwargs):
        """
        metodo abstrato reponsavel por validar os atributos
        passados para um metodo, levantando uma exceção caso o parametro
        seja invalido.

        """

        raise NotImplementedError

    @property
    def names(self):
        return [obj.name for obj in self]

    @property
    def types(self):
        return [obj.type for obj in self]

    @property
    def descriptions(self):
        return [obj.description for obj in self]

    def __dict__(self):
        """
        metodo que retorna um dicionario dos nomes e
        atributos da lista.

        :return: dict
        """

        return {attribute.name: attribute for attribute in self}

    def __str__(self):
        text = ""
        for attribute in self:
            text = text + attribute.__str__() + "\n"

        return text


class Path_atributes(Atrribute_list):
    def __init__(self, path_params):
        Atrribute_list.__init__(self, path_params)

    def validate(self, path_params):
        """
        Valida a lista de parametros obrigatorios.

        :param path_params: lista de parametros obrigatorios.
        :return: True or Exception.
        """

        if (len(path_params) != len(self)):
            raise AttributeSizeError(path_params, self)

        for path_param, path_attribute in zip(path_params, self):
            type_path_param = type(path_param)
            if (type_path_param != path_attribute.type):
                raise AttributeTypeError(type_path_param, path_attribute)

        return True


class Query_atributes(Atrribute_list):
    def __init__(self, query_params):
        Atrribute_list.__init__(self, query_params)

    def validate(self, query_params):
        """
        Valida a lista de parametros opcionais.

        :param query_params: dicionario dos parametros opcionais.
        :return: True or Exception.
        """
        query_params = {query_param_name: query_param_value for query_param_name, query_param_value in
                        query_params.items() if (query_param_value != None)}
        dict_attributes = self.__dict__()
        for query_param_name, query_param_value in query_params.items():
            query_param_type = type(query_param_value)
            if (query_param_name in dict_attributes):
                query_attribute = dict_attributes[query_param_name]
                if (query_attribute.type != query_param_type):
                    raise AttributeTypeError(query_param_type, query_attribute)
            else:
                raise AttributeNameError(query_param_name, self)

        return True
