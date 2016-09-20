# -*- coding: utf-8 -*-
from .scatter import Scatter
from .data import Data


class Scatter2D(Scatter):

    def __init__(self, **kwargs):
        self.data = Data(**kwargs)

    def plot(self):
        pass

    def save(init):
        pass
