# -*- coding: utf-8 -*-
from .scatter import Scatter
from .data import Data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Scatter2D(Scatter):

    def __init__(self, **kwargs):
        self.data = Data(**kwargs)
        plt.scatter(self.data.x, self.data.y)

    # TODO: make this works without breaking the tests
    # def __del__(self):
    #     plt.cla()

    def plot(self):
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()

    def save(self, name):
        plt.savefig(name)
