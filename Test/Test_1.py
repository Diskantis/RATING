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


# class Ui_ImageRating(object):
#     def setupUi(self, ImageRating):
#         # Главное окно приложения
#         ImageRating.setObjectName("ImageRating")
#         ImageRating.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
#         ImageRating.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#         ImageRating.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#         ImageRating.resize(1920, 1080)
#         ImageRating.move(1920, 0)
#
#         # Центральный виджет (все окно)
#         self.centralwidget = QtWidgets.QWidget(ImageRating)
#         self.centralwidget.setObjectName("centralwidget")
#
#         # слой вертекального выравнивания Центрального виджета (всего окна)
#         self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.v_Layout_centralwidget.setContentsMargins(10, 0, 10, 10)
#         self.v_Layout_centralwidget.setObjectName("verticalLayout")
#
#         # рамочка группы виджетов команд
#         self.frame_grb_items = QtWidgets.QFrame(self.centralwidget)
#         self.frame_grb_items.setMinimumSize(QtCore.QSize(580, 450))
#         self.frame_grb_items.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_grb_items.setObjectName("frame_items")
#
#         # слой вертекального выравнивания группы виджетов команд
#         self.v_Layout_grb_items = QtWidgets.QVBoxLayout(self.frame_grb_items)
#         self.v_Layout_grb_items.setObjectName("v_Layout_grb_items")
#
#         # прикрепляет группу виджетов к слою центрального виджета
#         self.v_Layout_centralwidget.addWidget(self.frame_grb_items)
