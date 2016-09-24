from .graphic import Graphic
from .data import Data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Line(Graphic):

    def __init__(self, **kwargs):
        self.data = Data(self.__init_data(**kwargs))
        self.__init_figure()

    def __init_figure(self):
        pass

    def __init_data(self, **kwargs):
        return {'x': kwargs['x'], 'y': kwargs['y']}

    def plot(self):
        pass

    def save(self):
        pass

    def x(self):
        return self.data.x

    def y(self):
        return self.data.y
