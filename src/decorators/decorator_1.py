"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"Add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji
"""
from functools import wraps


def require_typing(fn):
    def wrapper(*args, **kwargs):

        if len(list(fn.__code__.co_varnames))+1 != len(list(fn.__annotations__)):
            return (f'Add typing to function {fn.__name__}, please!')
        else:
            return fn(*args, **kwargs)
    return wrapper
