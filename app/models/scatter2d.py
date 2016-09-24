# -*- coding: utf-8 -*-
from .graphic import Graphic
from .data import Data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Scatter2D(Graphic):

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

    def add_subplot(self, **kwargs):
        args = Data(self.__init_data(**kwargs))
        self.ax.scatter(args.x, args.y)

    def save(self, name):
        plt.savefig(name)

    def x(self):
        return self.data.x

    def y(self):
        return self.data.y
