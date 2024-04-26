import unittest
import pylatform
import typing as t


@pylatform.schema
class ABC:
    a: int
    b: str = 1
    c: bool
    # d: t.Optional[int] not supported yet


class TestCLibSchema(unittest.TestCase):
    def test_libmodule(self):
        a = ABC()
        a.a = 10
        a.b = "hello"
        a.c = True

        try:
            a.a = "hello"
            assert False
        except ValueError:
            pass

        print(a)
