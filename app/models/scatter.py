# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Scatter(metaclass=ABCMeta):

    @abstractmethod
    def plot(self):
        pass
