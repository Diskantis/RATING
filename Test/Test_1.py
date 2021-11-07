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
        # self.setWindowTitle(name)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1920, 1080)
        self.move(1920, 0)

        # Центральный виджет (все окно)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")

        # слой вертекального выравнивания Центрального виджета (всего окна)
        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setObjectName("verticalLayout")

        self.image1 = QtWidgets.QLabel()
        pixmap1 = QPixmap('E:\\6_PROGRAMING\\1_PROJECT\\3_NEW PROJECT\\QT Creator\\RATING\\res\\КОМАНДА_АЛЕКСЕЙЧИК.png')
        # pixmap1 = pixmap1.scaledToWidth(1000)
        self.image1.setPixmap(pixmap1)
        # self.image1.setAlignment(QtCore.Qt.AlignCenter)
        self.image1.setObjectName("label")
        self.v_Layout_centralwidget.addWidget(self.image1)

        self.image2 = QtWidgets.QLabel()
        pixmap1 = QPixmap('E:\\6_PROGRAMING\\1_PROJECT\\3_NEW PROJECT\\QT Creator\\RATING\\res\\КОМАНДА_БУЯНА.png')
        # pixmap1 = pixmap1.scaledToWidth(1000)
        self.image2.setPixmap(pixmap1)
        self.image2.setAlignment(QtCore.Qt.AlignCenter)
        self.image2.setObjectName("label")
        self.v_Layout_centralwidget.addWidget(self.image2)

        self.image3 = QtWidgets.QLabel()
        pixmap1 = QPixmap('E:\\6_PROGRAMING\\1_PROJECT\\3_NEW PROJECT\\QT Creator\\RATING\\res\\КОМАНДА_ПОТАПОВОЙ.png')
        # pixmap1 = pixmap1.scaledToWidth(1000)
        self.image3.setPixmap(pixmap1)
        self.image3.setAlignment(QtCore.Qt.AlignCenter)
        self.image3.setObjectName("label")
        self.v_Layout_centralwidget.addWidget(self.image3)

        self.show()

    def close(self):
        self.close()


def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = ImageRating()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
