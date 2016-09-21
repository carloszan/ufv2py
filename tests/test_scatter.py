# -*- coding: utf-8 -*-
import pytest
from ..app.models.scatter2d import Scatter2D
import matplotlib.pyplot as plt


class TestScatter:

    def teardown_method(self, method):
        plt.cla()

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

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_scatter2d.png')
    def test_plot(self):
        s = Scatter2D(x=[1, 5], y=[3, 6])
        s.x_label('abscissa')
        s.y_label('ordenada')
        return plt

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_add_subplot_scatter2d.png')
    def test_add_data(self):
        s = Scatter2D(x=[1, 2], y=[3, 4])
        s.add_subplot(x=[5, 6], y=[4, 5])
        return plt
