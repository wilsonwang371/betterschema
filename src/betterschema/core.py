""" core module """

# pylint: disable=E0401, E0611
import logging
import typing as t

from betterschema.baselib import __schemas__, __watches__
from betterschema.baselib import schema as baseschema
from betterschema.baselib import watch as basewatch

logger = logging.getLogger(__name__)


class SelfType:
    """SelfType class"""

    def __repr__(self):
        return "SelfType()"

    def __str__(self):
        return "SelfType()"

    # we do not support instantiation of this class
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("SelfType is not instantiable")


Optional = t.Optional
Union = t.Union
SchemaSelf = SelfType


def is_schema_instance(schema_instance):
    """Check if the schema instance is a schema instance."""
    if type(schema_instance).__name__ not in __schemas__:
        return False
    return type(schema_instance).__name__ in __schemas__


def _schema(*args, **kwargs):
    """A decorator that allows you to define a schema class."""
    # either args length is 1 and kwargs is empty or args is empty and kwargs length is 1
    if len(args) == 1 and not kwargs:
        # make sure the args[0] is a class
        if not isinstance(args[0], type):
            raise ValueError("args must be a class")
        if not hasattr(args[0], "__annotations__"):
            raise ValueError("schema must be a class with __annotations__")
        res = baseschema(args[0])
        return res
    if not args and len(kwargs) == 1:
        # return a wrapper function that takes a class
        def wrapper(cls):
            if not isinstance(cls, type):
                raise ValueError("schema must be a class")
            if not hasattr(cls, "__annotations__"):
                raise ValueError("schema must be a class with __annotations__")
            res = baseschema(cls, kwargs)
            return res

        return wrapper
    raise ValueError("schema must be a class or a class with options")


def _watch(*args):
    """A decorator that allows you to define a watch function."""
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
        return basewatch(list(args), func)

    return wrapper


schema = _schema
watch = _watch


__all__ = [
    "Optional",
    "Union",
    "SchemaSelf",
    "schema",
    "watch",
    "__watches__",
    "__schemas__",
    "is_schema_instance",
]
