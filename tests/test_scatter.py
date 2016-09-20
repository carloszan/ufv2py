# -*- coding: utf-8 -*-
import pytest
from ..app.models.scatter2d import Scatter2D


class TestScatter:

    def test_plot(self):
        assert callable(Scatter2D.plot)
