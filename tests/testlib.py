import unittest
import pyskema
import typing as t


@pyskema.schema
class ABC:
    a: int
    b: str = 1
    c: bool
    # d: t.Optional[int]  # not supported yet


class TestCLibSchema(unittest.TestCase):
    def test_libmodule(self):
        print(str(ABC.__annotations__))

        a = ABC(
            {
                "a": 10,
                "b": "hello",
                "c": True,
            }
        )
        print(a.b)

        print(a.__annotations__)
        a.a = 10
        a.b = "hello"
        a.c = True

        try:
            a.nonexistent = 10
            assert False
        except AttributeError:
            pass

        print(a.a)
        print(a.b)
        print(a.c)

        try:
            a.a = "hello"
            assert False
        except TypeError:
            pass

        # a.abc = "world"


if __name__ == "__main__":
    unittest.main()
