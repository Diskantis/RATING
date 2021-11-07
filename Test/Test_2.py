# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QPushButton, QProgressBar
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint, QSize, Qt, QTimeLine, QObject, \
    QEasingCurve, QSequentialAnimationGroup, QRect


# class ImageTeam(QWidget):
#     def __init__(self, path_1):
#         super().__init__()
#
#         v_Layout_item = QtWidgets.QVBoxLayout()
#         image_team_1 = QtWidgets.QLabel()
#         image_team_1.setFixedSize(1024, 128)
#         image_team_1.setScaledContents(True)
#         pixmap = QPixmap(path_1)
#         image_team_1.setPixmap(pixmap)
#         image_team_1.setObjectName("image_team")
#         v_Layout_item.addWidget(image_team_1, 0, QtCore.Qt.AlignHCenter)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1080)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.activateWindow()

        self.v_Layout_grb_items_rat = QtWidgets.QVBoxLayout(self)
        self.v_Layout_grb_items_rat.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.v_Layout_grb_items_rat.setContentsMargins(0, 0, 0, 0)
        self.v_Layout_grb_items_rat.setSpacing(0)
        self.v_Layout_grb_items_rat.setObjectName("v_Layout_grb_items")

        path_1 = "D:/5_MICHAEL/1_PROJECT/QT Creator/RATING/res/КОМАНДА_АЛЕКСЕЙЧИК.png"
        path_2 = "D:/5_MICHAEL/1_PROJECT/QT Creator/RATING/res/КОМАНДА_ПОТАПОВОЙ.png"

        self.image_team_1 = QtWidgets.QLabel(self)
        self.image_team_1.resize(1024, 128)
        self.image_team_1.setScaledContents(True)
        self.pixmap_1 = QPixmap(path_1)
        self.image_team_1.setPixmap(self.pixmap_1)
        self.image_team_1.setObjectName("image_team")
        # self.v_Layout_grb_items_rat.addWidget(self.image_team_1, 0, QtCore.Qt.AlignVCenter)

        self.image_team_2 = QtWidgets.QLabel(self)
        self.image_team_2.setFixedSize(1024, 128)
        self.image_team_2.setScaledContents(True)
        self.pixmap_2 = QPixmap(path_2)
        self.image_team_2.setPixmap(self.pixmap_2)
        self.image_team_2.setObjectName("image_team")
        self.v_Layout_grb_items_rat.addWidget(self.image_team_2, 0, QtCore.Qt.AlignHCenter)

        self.anim_1 = QPropertyAnimation(self.image_team_1, b"geometry")

        self.anim_1.setKeyValueAt(0, QRect(self.image_team_1.x(), self.image_team_1.y(), 1024, 128))
        self.anim_1.setKeyValueAt(0.5, QRect(self.image_team_1.x(), int(self.image_team_2.y() / 2),
                                             int(1024 * 1.2), int(128 * 1.2)))
        self.anim_1.setKeyValueAt(1, QRect(self.image_team_2.x(), self.image_team_2.y(), 1024, 128))
        # self.anim.setEndValue(QPoint(int(1920/2-(1024/2)), int(1080/2)))
        self.anim_1.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim_1.setDuration(2000)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        # self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
