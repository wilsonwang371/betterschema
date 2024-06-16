"""Test render module."""

# pylint: disable=E1101, R0903, E1136, E0401
import unittest

from betterschema import core, render


@core.schema(mapping={"x": "a", "y": "b", "z": "c"})
class DEFA2:
    """DEF schema"""

    x: int
    y: str
    z: bool


@core.schema
class ABCD2:
    """ABC schema"""

    a: int
    b: str = 1
    c: bool
    d: list[str]
    # d: t.Optional[int]  # not supported yet
    e: DEFA2


class TestCore(unittest.TestCase):
    """Test core module"""

    def test_rendermodule(self):
        """Test render module"""

        print(str(ABCD2.__annotations__))

        a = ABCD2(
            {
                "a": 10,
                "b": "hello",
                "c": True,
                "d": ["a", "b", "c"],
                "e": {
                    "x": 10,
                    "y": "hello",
                    "z": True,
                },
            }
        )

        y = render.render(a)
        j = render.render(a, render.RenderType.JSON)

        print(y)
        print(j)
