from datetime import datetime

def time_to_milliseconds(time):
    """
    Pega um tempo passando nos formatos de string,datetime(python)
    ou lista, e converte para milegundos.
    Para o formato de string, a formatação de time devera ser da 
    seguinte maneira:
        time = "dia/mes/ano", com o ano sem abreviações, como por exemplo
        time = "10/12/2013".
    Para o formato de lista ou tuple o formato devera ser:
        time = (ano,mês,dia)

    :param time: tempo a ser convertido para segundos.
    :return int: tempo convertido.

    """
    if(time!=None):
        if isinstance(time, datetime):
            time = time.timestamp()
        elif isinstance(time, str):
            time = datetime.strptime(time, "%d/%m/%Y").timestamp()
        elif isinstance(time, list) or isinstance(time, tuple):
            time = datetime(time).timestamp()
        else:
            raise TypeError("time of type {0} is not supported".format(type(time).__name__))

        time = int(time)
    

    return time
