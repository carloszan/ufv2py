# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from ..helpers.imports import *
import matplotlib.pyplot as plt


class Graph(metaclass=ABCMeta):

    # # refactor?
    # @abstractmethod
    # def __init_figure(self):
    #     pass
    #
    # # refactor?
    # @abstractmethod
    # def add_subplot(self, kwargs={}):
    #     args = Data(kwargs)

    def plot(self):
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()

    @abstractmethod
    def save(self, name):
        pass

    def x_label(self, label):
        self.x_label = label

    def y_label(self, label):
        self.y_label = label
