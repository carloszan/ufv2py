# -*- coding: utf-8 -*-
from .scatter import Scatter
from .data import Data
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt


class Scatter2D(Scatter):

    def __init__(self, **kwargs):
        self.data = Data(**kwargs)
        # self.plt = scatter(data.x, data.y)

    def plot(self):
        plt.xlabel(self.x_label)
        plt.xlabel(self.y_label)
        # self.plt.show()
        pass

    def save(self, name):
        # self.plt.savefig(name)
        pass
