# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):

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
