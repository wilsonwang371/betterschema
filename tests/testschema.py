import core.schema as schema
import typing as t
import unittest


@schema.define
class Foo:
    foo1: str
    foo2: int
    foo3: bool
    foo4: list[str]
    foo5: t.Optional[int]
    foo6: dict[str, int]

    @schema.define
    class EmbeddedSchema:
        bar1: str
        bar2: int
        bar3: bool

    bar: EmbeddedSchema


@schema.check(Foo, Foo.foo1)
def check_foo1(value: str) -> bool:
    return value == "hello" or value == "world"


class TestSchema(unittest.TestCase):

    def test_schema(self):
        # not supported yet
        # foo = Foo(
        #     {
        #         "foo1": "hello",
        #         "foo2": 0,
        #         "foo3": True,
        #         "foo4": ["a", "b", "c"],
        #         "bar": Foo.EmbeddedSchema(
        #             {
        #                 "bar1": "world",
        #                 "bar2": 20,
        #                 "bar3": False,
        #             }
        #         ),
        #     }
        # )
        foo = Foo()
        foo.foo1 = "hello"
        foo.foo2 = 0
        foo.foo3 = True
        foo.foo4 = ["a", "b", "c"]
        foo.bar = Foo.EmbeddedSchema()
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

        try:
            foo.foo1 = "world"
        except ValueError as e:
            raise AssertionError("ValueError not raised")

        try:
            foo.foo1 = "hi"
        except ValueError as e:
            pass
        else:
            raise AssertionError("ValueError not raised")

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
