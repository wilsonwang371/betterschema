"""Test render module."""

# pylint: disable=E1101, R0903, E1136, E0401
import unittest

from betterschema import core, render


@core.schema
class DEF2:
    """DEF schema"""

    x: int
    y: str
    z: bool


@core.schema
class ABC2:
    """ABC schema"""

    a: int
    b: str = 1
    c: bool
    d: list[str]
    # d: t.Optional[int]  # not supported yet
    e: DEF2


class TestCore(unittest.TestCase):
    """Test core module"""

    def test_rendermodule(self):
        """Test render module"""

        print(str(ABC2.__annotations__))

        a = ABC2(
            {
                "a": 10,
                "b": "hello",
                "c": True,
                "d": ["x", "y", "z"],
                "e": {
                    "x": 30,
                    "y": "hi",
                    "z": True,
                },
            }
        )
        render.render(a)
        render.render(a, render.RenderType.JSON)
