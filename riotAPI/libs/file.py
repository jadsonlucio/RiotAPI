import os
import json

from PIL import Image
from os.path import isfile,join
from .. import __path__


__all__=["create_file","read_file","isfile","set_abs_path"]


def create_file(path,data,file_type):
    path=join(get_abs_path(),path)
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as file:
        if(file_type=="json"):
            json.dump(data,file)
        elif(file_type=="image"):
            data.save(file)

def read_file(path,data_type):
    data=None
    if(data_type=="json"):
        with open(path,'r') as file:
            file.seek(0)
            data=json.load(file)
    elif(data_type=="image"):
        data=Image.open(path)

    return data

def get_abs_path():
    return __path__[0]

def set_abs_path(path):
    return join(__path__[0],path)