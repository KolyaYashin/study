from typing import Callable
from collections.abc import Hashable
import collections


def memoize(f):
    cache = {}

    def make_hashable(obj):
        """Make a hashable version of the object."""
        if isinstance(obj, (tuple, list)):
            return tuple(make_hashable(e) for e in obj)
        if isinstance(obj, dict):
            return tuple((k, make_hashable(v)) for k, v in sorted(obj.items()))
        if isinstance(obj, set):
            return tuple(make_hashable(e) for e in sorted(obj))
        if isinstance(obj, collections.abc.Hashable):
            return obj
        raise TypeError(f'Object of type {type(obj)} is not hashable.')

    def decorate(*args, **kwargs):

        key = (make_hashable(args), make_hashable(kwargs))
        if key not in cache:
            cache[key] = f(*args, **kwargs)

        return cache[key]

    return decorate


@memoize
def fib(*args, **kwargs):
    print(args)
    print(kwargs)
    return len(args) + len(kwargs)


print('f =', fib(2))
print('f =', fib(3, 2))
print('f =', fib(3, 2, name='Kolya', surname='Yashin'))

print('f =', fib({'a': 2}, {'b': 3}, hi='hello', name='Kolya'))

print('f =', fib({'a': 2}, hi={'a': 2}, name='Kolya'))

print('f =', fib([], set([1,2,3]) , hi = 'hello', name = 'Kolya'))

