from functools import wraps
import re
from typing import Callable

RE_NOP = re.compile('^_|[a-z]', re.A)


def run_once(fun: Callable) -> Callable:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if not wrapper._done:
            wrapper._done = True
            return fun(*args, **kwargs)

    wrapper._done = False
    return wrapper


def should_copy(a: str) -> bool:
    return a.isidentifier() and RE_NOP.search(a) is None
