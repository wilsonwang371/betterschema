import unittest
import pyskema.core as core
import pyskema.render as render


@core.schema
class DEF2:
    x: int
    y: str
    z: bool


@core.schema
class ABC2:
    a: int
    b: str = 1
    c: bool
    # d: t.Optional[int]  # not supported yet
    e: DEF2


class TestCore(unittest.TestCase):
    def test_rendermodule(self):
        print(str(ABC2.__annotations__))

        a = ABC2(
            {
                "a": 10,
                "b": "hello",
                "c": True,
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
