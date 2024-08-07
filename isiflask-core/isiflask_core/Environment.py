import os
from functools import wraps
from typing import Any, Callable

def env(env_key: str, default_value: Any) -> Any:
    """ Parsea el valor de una variable de entorno a una variable utilizable para python

    Args:
        env_key (str): Nombre de la variable de entorno de
        default_value (Any): Valor por default de la variable de entorno

    Returns:
        Any: Valor designado de la variable de entorno o en su defecto la default
    """
    if env_key in os.environ:
        if os.environ[env_key].isdecimal():
            return int(os.environ[env_key])
        elif str(os.environ[env_key]).lower() == "true" or str(os.environ[env_key]).lower() == "true":
            return str(os.environ[env_key]).lower() == "true"
        else:
            return os.environ[env_key]
    else:
        return default_value

def reload_env_vars(function: Callable):
    @wraps(function)
    def decorator(*args, **kwargs):
        global APP_URL
        APP_URL     = env("APP_URL", "")
        
        function(*args, **kwargs)

    return decorator

APP_URL     = env("APP_URL", "")
