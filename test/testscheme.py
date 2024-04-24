import core.scheme as scheme
import typing as t
import unittest

@scheme.define
class Foo:
    foo1: str
    foo2: int
    foo3: bool
    foo4: t.List[str]

    @scheme.define
    class EmbeddedScheme:
        bar1: str
        bar2: int
        bar3: bool
    bar: EmbeddedScheme

class TestScheme(unittest.TestCase):

    def test_scheme(self):
        foo = Foo()
        foo.foo1 = "hello"
        foo.foo2 = 0
        foo.foo3 = True
        foo.foo4 = ["a", "b", "c"]
        foo.bar = Foo.EmbeddedScheme()
        foo.bar.bar1 = "world"
        foo.bar.bar2 = 20
        foo.bar.bar3 = False

        assert foo.foo1 == "hello"
        assert foo.foo2 == 0
        assert foo.foo3 == True
        assert foo.foo4 == ["a", "b", "c"]
        assert foo.bar.bar1 == "world"
        assert foo.bar.bar2 == 20
        assert foo.bar.bar3 == False

        foo <<= {"foo2": 1}
        assert foo.foo2 == 1

        foo <<= {"foo2": 2, "foo3": False}
        assert foo.foo2 == 2
        assert foo.foo3 == False

        foo <<= {"foo4": ["d", "e", "f"]}
        assert foo.foo4 == ["d", "e", "f"]

        foo <<= {"bar": {"bar1": "hello", "bar2": 10, "bar3": True}}
        assert foo.bar.bar1 == "hello"
        assert foo.bar.bar2 == 10
        assert foo.bar.bar3 == True

        try:
            foo <<= {"random": "value"}
        except AttributeError as e:
            pass
        else:
            raise AssertionError("ValueError not raised")

        try:
            foo <<= {"foo2": "value"}
        except ValueError as e:
            pass
        else:
            raise AssertionError("ValueError not raised")

        try:
            foo <<= {"foo4": "value"}
        except ValueError as e:
            pass
        else:
            raise AssertionError("ValueError not raised")

        try:
            foo <<= {"bar": "value"}
        except ValueError as e:
            pass
        else:
            raise AssertionError("ValueError not raised")

        foo <<= {"bar": {"bar1": "hello", "bar2": 10, "bar3": "value"}}


if __name__ == "__main__":
    unittest.main()