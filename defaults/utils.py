from functools import wraps
import re
from typing import Callable


def run_once(fun: Callable) -> Callable:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if not wrapper._done:
            if not ('finalize_settings' in kwargs and kwargs['finalize_settings'] is False):
                wrapper._done = True
            return fun(*args, **kwargs)

    wrapper._done = False
    return wrapper


def should_copy(a: str) -> bool:
    return a.isidentifier() and not a.startswith('_') and a.isupper()
