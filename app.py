# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from app.helpers.data_dealers import str_to_list_of_int
from app.models.scatter2d import Scatter2D


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.__initUI()

    def __initUI(self):
        self.setGeometry(350, 200, 600, 500)
        self.setWindowTitle("ufv2py")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Graficos')
        plotagem = fileMenu.addMenu('Plotagem')
        plotagem.addAction('2D', self.open_csv)



        self.show()

    def open_csv(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        data = None

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()

        x, y = str_to_list_of_int(data)


def main():
    app = QApplication(sys.argv)

    # Start the app
    GUI = Window()
    # GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
