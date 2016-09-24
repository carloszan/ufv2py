# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):

    # # refactor?
    # @abstractmethod
    # def __init_figure(self):
    #     pass
    #
    # # refactor?
    # @abstractmethod
    # def __add_subplot(self, place):
    #     pass

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def save(self, name):
        pass

    def x_label(self, label):
        self.x_label = label

    def y_label(self, label):
        self.y_label = label
