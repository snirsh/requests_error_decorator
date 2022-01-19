import inspect
import logging

import requests


def requests_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as err:
            func_args = inspect.signature(func).bind(*args, **kwargs).arguments
            func_args_str = ", ".join(map("{0[0]} = {0[1]!r}".format, func_args.items()))
            func_repr = f"{func.__module__}.{func.__qualname__} ({func_args_str})"
            logging.error(f"{func_repr}\n{err}")
            return err.response

    return wrapper
