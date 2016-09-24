import pytest
from ..app.models.graphic import Graphic


class TestGraphic:

    def test_method_calls(self):
        assert callable(Graphic.save)
        assert callable(Graphic.plot)
