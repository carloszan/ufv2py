from .graph import Graph
from .data import Data
from ..helpers.imports import *
import matplotlib.pyplot as plt


class Line(Graph):

    def __init__(self, **kwargs):
        self.data = Data(self.__init_data(**kwargs))
        self.__init_figure()

    def __init_figure(self):
        self.fig = plt.figure()
        self.ax = self.__add_subplot(111)
        self.ax.plot(self.x(), self.y())

    def __add_subplot(self, place):
        return self.fig.add_subplot(place)

    def __init_data(self, **kwargs):
        return {'x': kwargs['x'], 'y': kwargs['y']}

    def add_plot(self, **kwargs):
        args = Data(self.__init_data(**kwargs))
        self.ax.plot(args.x, args.y, kwargs['color'])

    def save(self):
        plt.save()

    def x(self):
        return self.data.x

    def y(self):
        return self.data.y
