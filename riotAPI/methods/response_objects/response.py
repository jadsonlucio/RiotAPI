import numpy as np

class Response(object):
    """
    Super-classe das classes que representam os objetos retornados pelas
    requisições aos metodos da api

    """

    def __init__(self, **kwargs):
        """
        Inicializa um objeto convertendo todos os argumentos do dicionario **kwargs em
        variaveis .

        :param kwargs: dicionario que representa as variaveis presentes nos objetos dessa classe
        """

        self.params = kwargs
        for key, value in zip(kwargs.keys(), kwargs.values()):
            self.__setattr__(key, value)

    def __str__(self):
        """
        Metodo magico que retorna uma string
        contendo todos os parametros que foram passados
        pro metodo __init__.

        :return: String
        """

        return str(self.params)

    def __getitem__(self, item):
        if (isinstance(item, str)):
            return self.__getattr__(item)

    def __getattr__(self, item):
        if (hasattribute(self, item)):
            return self.__getattribute__(item)
        else:
            dict_vars = self.to_dict()
            if (item in dict_vars):
                return dict_vars[item]
            else:
                raise AttributeError("{0} object has no attribute {1}".format(self.__class__.__name__,item))

    def to_dict(self):
        dict = {}
        for key, obj in vars(self).items():
            if (isinstance(obj, Response)):
                dict = {**dict, **obj.to_dict()}
            else:
                dict[key] = obj

        return dict


class Response_list(list):
    """
    Super-classe das classes que representam um lista de objetos do
    tipo Response

    """

    def load_response_object(self, kwargs):
        """
        Metodo abstrato responsavel por carregar um objeto do tipo
        especificado pelo Response_list

        :param kwargs: dicionario que representa as variaveis presentes nos objetos dessa classe
        :return: Response
        """
        raise NotImplementedError

    def __init__(self, list_kwargs=None, list_objects=None, **kwargs):
        """
        Inicializar um objeto do tipo Response_list

        :param list_kwargs: lista ou dicionario contendo atributos para
        criar novos objetos que vao ser adicionados ao Response_list
        :param kwargs: dicionario que representa as variaveis presentes nos objetos dessa classe
        """

        list.__init__(self)
        self.params = kwargs
        self.__params = list_kwargs

        for key, value in zip(kwargs.keys(), kwargs.values()):
            self.__setattr__(key, value)

        if (list_objects != None):
            [self.append(obj) for obj in list_objects]
        if (list_kwargs != None and isinstance(list_kwargs, list)):
            for kwargs in list_kwargs:
                self.append(self.load_response_object(kwargs))
        elif (list_kwargs != None and isinstance(list_kwargs, dict)):
            for kwargs in list_kwargs.values():
                self.append(self.load_response_object(kwargs))

    def __getitem__(self, item):
        if (isinstance(item, str)):
            return self.__getattr__(item)
        else:
            return list.__getitem__(self, item)

    def __getattr__(self, item):
        if (hasattribute(self, item)):
            return object.__getattribute__(self, item)
        else:
            attribute_list = []
            for obj in self:
                attribute_list.append(obj[item])
            return np.array(attribute_list)

    def to_dict(self):
        dict_array = [obj.to_dict() for obj in self]
        dict_array = np.array(dict_array).ravel()
        dict_array = [{**dict, **vars(self)} for dict in dict_array]

        return dict_array


def hasattribute(obj, name):
    if (name in vars(obj)):
        return True
    else:
        return False


def isresponseinstance(obj):
    if (isinstance(obj, Response) or isinstance(obj, Response_list)):
        return True
    else:
        return False