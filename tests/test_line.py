# -*- coding: utf-8 -*-
import pytest
from ..app.models.line import Line
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class TestLine:

    def setup_method(self):
        self.l = Line(x=[1, 2], y=[3, 2])

    def teardown_method(self, method):
        plt.cla()

    def test_init(self):
        assert self.l.x() == [1, 2]
        assert self.l.y() == [3, 2]

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_line.png')
    def test_line_plot(self):
        x_points = list(range(50))
        y_points = list(range(50))
        l = Line(x=x_points, y=y_points)
        l.x_label('abscissa')
        l.y_label('ordenada')
        return plt

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_function_line.png')
    def test_function_line(self):
        # function: 2^n
        x_points = list(range(1, 11))
        y_points = [2**x for x in list(range(1, 11))]
        l = Line(x=x_points, y=y_points)
        l.x_label('abscissa')
        l.y_label('ordenada')
        return plt

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_comparison_line.png')
    def test_comparison_line(self):
        x_points = list(range(50))
        y_points = list(range(50))
        l = Line(x=x_points, y=y_points)
        x2_points = list(range(1, 11))
        y2_points = [2**x for x in list(range(1, 11))]
        l.add_subplot(x=x2_points, y=y2_points, color='r')
        return plt
