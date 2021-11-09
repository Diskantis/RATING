# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ImageRating(QtWidgets.QWidget):
    def __init__(self):
        super(ImageRating, self).__init__()

        self.setObjectName("ImageRating")
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1920, 1080)
        self.move(1920, 0)




def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = ImageRating()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
