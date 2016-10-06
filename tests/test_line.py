# -*- coding: utf-8 -*-
import pytest
from ..app.models.line import Line
import matplotlib.pyplot as plt


# function: 2^n
def two_power_n():
    return [2**x for x in list(range(1, 11))]


# function: n^2
def n_power_two():
    return [x**2 for x in list(range(1, 11))]


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
        x_points = list(range(1, 11))
        y_points = two_power_n()
        l = Line(x=x_points, y=y_points)
        l.x_label('abscissa')
        l.y_label('ordenada')
        return plt

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_comparison_line.png')
    def test_comparison_line(self):
        x_points = list(range(11))
        y_points = list(range(11))
        l = Line(x=x_points, y=y_points)
        x2_points = list(range(1, 11))
        y2_points = two_power_n()
        l.add_plot(x=x2_points, y=y2_points, color='r')
        return plt

    @pytest.mark.mpl_image_compare(baseline_dir='baseline',
                                   filename='test_comparison_2_line.png')
    def test_comparison_2_line(self):
        x_points = list(range(11))
        y_points = list(range(11))
        l = Line(x=x_points, y=y_points)
        x2_points = list(range(1, 11))
        y2_points = two_power_n()
        l.add_plot(x=x2_points, y=y2_points, color='r')
        x3_points = list(range(1, 11))
        y3_points = n_power_two()
        l.add_plot(x=x3_points, y=y3_points, color='g')
        return plt
