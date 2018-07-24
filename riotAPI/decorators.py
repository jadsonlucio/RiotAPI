from time import ctime
from .exceptions.response import RateLimitExceeded


def api_method(api_method_func):
    def wrapper(riotAPI, id, region=None, **kwargs):
        try:
            if (region == None):
                region = riotAPI.region

            return api_method_func(riotAPI, id, region=region, **kwargs)
        except RateLimitExceeded as e:
            riotAPI.api_key_index = (riotAPI.api_key_index + 1) % riotAPI.api_keys_size

    return wrapper


def ddragon_method(**kwargs):
    def ddragon_method_decorator(ddragon_mathod_func):
        def wrapper(riotAPI, default_method_kwargs=kwargs, *args, **kwargs):
            if ("language" in default_method_kwargs and "language" not in kwargs):
                default_method_kwargs["language"] = riotAPI.language
            elif ("language" in default_method_kwargs):
                default_method_kwargs.pop("language")
            kwargs.update(default_method_kwargs)
            return ddragon_mathod_func(riotAPI, *args, **kwargs)

        return wrapper

    return ddragon_method_decorator
