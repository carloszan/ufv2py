import pytest
from ..app.models.graph import Graph


class TestGraph:

    def test_method_calls(self):
        assert callable(Graph.save)
        assert callable(Graph.plot)
