# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1080)
        self.move(1920, 0)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.activateWindow()

        self.v_Layout_grb_items_rat = QtWidgets.QVBoxLayout(self)
        self.v_Layout_grb_items_rat.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.v_Layout_grb_items_rat.setContentsMargins(0, 0, 0, 0)
        self.v_Layout_grb_items_rat.setSpacing(0)
        self.v_Layout_grb_items_rat.setObjectName("v_Layout_grb_items")

        self.image_team_1 = QtWidgets.QLabel(self)
        self.image_team_1.resize(1024, 128)
        self.image_team_1.setScaledContents(True)
        self.pixmap_1 = QPixmap("E:/6_PROGRAMING/1_PROJECT/3_NEW PROJECT/QT Creator/RATING/res/КОМАНДА_АЛЕКСЕЙЧИК.png")
        self.image_team_1.setPixmap(self.pixmap_1)
        self.v_Layout_grb_items_rat.addWidget(self.image_team_1, 0, QtCore.Qt.AlignCenter)

        # self.animation = QPropertyAnimation(self.image_team_1, b"geometry")
        # self.animation.setDuration(2000)
        # # self.animation.setStartValue(QRect(10, 10, 100, 30))
        # self.animation.setKeyValueAt(0, QRect(0, 0, 100, 30))
        # self.animation.setKeyValueAt(0.5, QRect(125, 125, 200, 60))
        # self.animation.setKeyValueAt(1, QRect(250, 250, 100, 30))
        # # self.animation.setEndValue(QRect(250, 250, 100, 30))
        # self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        #
        # self.animation.start()


def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
