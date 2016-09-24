# -*- coding: utf-8 -*-
import pytest
from ..app.models.line import Line
import matplotlib.pyplot as plt


class TestLine:

    def setup_method(self):
        self.l = Line(x=[1, 2], y=[3, 2])

    def test_init(self):
        assert self.l.x() == [1, 2]
        assert self.l.y() == [3, 2]
