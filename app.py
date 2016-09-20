# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.__initUI__()

    def __initUI__(self):
        self.setGeometry(350, 200, 600, 500)
        self.setWindowTitle("ufv2py")
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication(sys.argv)

    # Start the app
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
