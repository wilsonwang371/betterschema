import logging
import pyskema.baselib as baselib

logger = logging.getLogger(__name__)


def _schema(cls):
    # make sure the cls is a class with __annotations__
    if not isinstance(cls, type):
        raise ValueError("schema must be a class")
    if not hasattr(cls, "__annotations__"):
        raise ValueError("schema must be a class with __annotations__")
    res = baselib.schema(cls)
    return res


def _watch(*args):
    # make sure the args is a list of tuples
    for arg in args:
        if not isinstance(arg, tuple):
            raise ValueError("args must be a list of tuples")
        # make sure the first element of the tuple is a class
        if not isinstance(arg[0], type):
            raise ValueError(
                "args must be a list of tuples with the first element as a class"
            )
        # make sure the second element of the tuple is a string
        if not isinstance(arg[1], str):
            raise ValueError(
                "args must be a list of tuples with the second element as a string"
            )

    def wrapper(func):
        return baselib.watch(list(args), func)

    return wrapper


schema = _schema
watch = _watch

__watches__ = baselib.__watches__
__schemas__ = baselib.__schemas__

__all__ = ["schema", "watch", "__watches__", "__schemas__"]
