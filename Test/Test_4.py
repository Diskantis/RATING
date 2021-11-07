import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)

        self.button = QPushButton("Animated Button", self)
        self.button.show()

        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(2000)
        # self.animation.setStartValue(QRect(10, 10, 100, 30))
        self.animation.setKeyValueAt(0, QRect(0, 0, 100, 30))
        self.animation.setKeyValueAt(0.5, QRect(125, 125, 200, 60))
        self.animation.setKeyValueAt(1, QRect(250, 250, 100, 30))
        # self.animation.setEndValue(QRect(250, 250, 100, 30))
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.animation.start()


def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = Window()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
