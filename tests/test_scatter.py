# -*- coding: utf-8 -*-
import pytest
from ..app.models.scatter2d import Scatter2D
import matplotlib.pyplot as plt


class TestScatter:

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_scatter2d.png')
    def test_plot(self):
        s = Scatter2D(x=[1, 5], y=[3, 6])
        s.x_label('abscissa')
        s.y_label('ordenada')
        return plt

    def test_method_calls(self):
        assert callable(Scatter2D.save)
        assert callable(Scatter2D.plot)

    def test_init(self):
        s = Scatter2D(x=[1, 1], y=[1, 2])
        assert s.data.x == [1, 1]
        assert s.data.y == [1, 2]

    def test_labels(self):
        s = Scatter2D(x=[1, 1], y=[1, 2])
        s.x_label('abscissa')
        s.y_label('ordenada')
        assert s.x_label == 'abscissa'
        assert s.y_label == 'ordenada'
