# -*- coding: utf-8 -*-
import pytest
from ..app.models.scatter2d import Scatter2D


class TestScatter:

    def test_plot(self):
        assert callable(Scatter2D.plot)
        assert callable(Scatter2D.save)

    def test_init(self):
        s = Scatter2D(x=[1, 1], y=[1, 2], z=[1, 3])
        assert s.data.x == [1, 1]
        assert s.data.y == [1, 2]
        assert s.data.z == [1, 3]

        s = Scatter2D(x=[1, 1], y=[1, 2])
        with pytest.raises(AttributeError):
            assert s.data.z == [1, 3]

    def test_labels(self):
        s = Scatter2D(x=[1, 1], y=[1, 2], z=[1, 3])
        s.x_label('abscissa')
        s.y_label('ordenada')
        assert s.x_label == 'abscissa'
        assert s.y_label == 'ordenada'
