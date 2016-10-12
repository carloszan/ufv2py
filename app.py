# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from app.helpers.data_dealers import *
from app.models.scatter2d import Scatter2D
from app.models.line import Line


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.__initUI()

    def __initUI(self):
        self.setGeometry(350, 200, 600, 500)
        self.setWindowTitle("ufv2py")

        menubar = self.menuBar()
        file_menu = menubar.addMenu('Graficos')
        plots = file_menu.addMenu('Plotagem')

        plots.addAction('Scatter 2D', self.plot_s2d)
        plots.addAction('Line', self.plot_line)

        self.show()

    def plot_s2d(self):
        f = self.__open_csv()

        x, y = csv_to_array(f)
        s = Scatter2D(x=x, y=y)
        s.plot()

    def plot_line(self):
        f = self.__open_csv()

        x, y = csv_to_array(f)
        s = Line(x=x, y=y)
        s.plot()

    def __open_csv(self):
        fname = QFileDialog.getOpenFileName(self, 'Open CSV')
        f = None

        if fname[0]:
            f = open(fname[0], 'r')
        return f


def main():
    app = QApplication(sys.argv)

    # Start the app
    GUI = Window()
    # GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
