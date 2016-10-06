# -*- coding: utf-8 -*-
from .graph import Graph
from .data import Data
# to build succeed we have to put these lines
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Scatter2D(Graph):

    def __init__(self, **kwargs):
        self.data = Data(self.__init_data(**kwargs))
        self.__init_figure()

    def __init_figure(self):
        self.fig = plt.figure()
        self.ax = self.__add_subplot(111)
        self.ax.scatter(self.data.x, self.data.y)

    def __add_subplot(self, place):
        return self.fig.add_subplot(place)

    # def __del__(self):
    #     plt.cla()

    def __init_data(self, **kwargs):
        return {'x': kwargs['x'], 'y': kwargs['y']}

    def add_plot(self, **kwargs):
        args = Data(self.__init_data(**kwargs))
        self.ax.scatter(args.x, args.y)

    def save(self, name):
        plt.savefig(name)

    def x(self):
        return self.data.x

    def y(self):
        return self.data.y
