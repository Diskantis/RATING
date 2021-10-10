# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class Add_Team(QtWidgets.QDialog):
    def __init__(self):
        super(Add_Team, self).__init__()

        self.setObjectName("Add_item")
        self.setWindowTitle("Add new item")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(400, 210)
        self.setMinimumSize(QtCore.QSize(400, 210))
        self.setMaximumSize(QtCore.QSize(400, 210))
        self.setStyleSheet("background-color: rgb(78, 79, 84); color: rgb(209, 209, 217);")

        font = QtGui.QFont()
        font.setPointSize(10)

        self.grb_item_prp = QtWidgets.QGroupBox("Item properties:", self)
        self.grb_item_prp.setGeometry(QtCore.QRect(10, 10, 380, 150))
        self.grb_item_prp.setObjectName("groupBox")
        font_grp = QtGui.QFont()
        font_grp.setPointSize(10)
        font_grp.setBold(True)
        font_grp.setUnderline(True)
        self.grb_item_prp.setFont(font_grp)
        self.grb_item_prp.setStyleSheet("QGroupBox {border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);} ")
        self.grb_item_prp.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_item_prp.setObjectName("grb_item_prp")

        self.frame_image = QtWidgets.QFrame(self.grb_item_prp)
        self.frame_image.setGeometry(QtCore.QRect(1, 40, 378, 50))
        self.frame_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_image.setObjectName("frame")

        self.h_Layout_frame_image = QtWidgets.QHBoxLayout(self.frame_image)
        self.h_Layout_frame_image.setContentsMargins(10, 0, 10, 0)
        self.h_Layout_frame_image.setObjectName("h_Layout_frame_image")

        self.line_image = QtWidgets.QLineEdit(self.frame_image)
        self.line_image.setMinimumSize(QtCore.QSize(0, 30))
        self.line_image.setFont(font)
        self.line_image.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                      "border: 1px solid rgba(50, 50, 50, 240); "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                      "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_image.setObjectName("lineEdit")
        self.h_Layout_frame_image.addWidget(self.line_image)

        self.btn_brow_image = QtWidgets.QPushButton("Browse...", self.frame_image)
        self.btn_brow_image.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_brow_image.setFont(font)
        self.btn_brow_image.setObjectName("pushButton")
        self.h_Layout_frame_image.addWidget(self.btn_brow_image)

        self.label_image = QtWidgets.QLabel("Image:", self.grb_item_prp)
        self.label_image.setGeometry(QtCore.QRect(12, 20, 355, 30))
        self.label_image.setFont(font)
        self.label_image.setObjectName("label")

        # FRAME OK ADD_NEW_ITEM
        self.frame_ok = QtWidgets.QFrame(self)
        self.frame_ok.setEnabled(True)
        self.frame_ok.setGeometry(QtCore.QRect(0, 160, 400, 50))
        self.frame_ok.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ok.setObjectName("frame_ok")

        self.h_Layout_ok = QtWidgets.QHBoxLayout(self.frame_ok)
        self.h_Layout_ok.setObjectName("h_Layout_ok")

        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_ok.addItem(spacerItem1)

        self.btn_cancel = QtWidgets.QPushButton("Cancel", self.frame_ok)
        self.btn_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_Layout_ok.addWidget(self.btn_cancel)

        self.btn_ok = QtWidgets.QPushButton("OK", self.frame_ok)
        self.btn_ok.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.h_Layout_ok.addWidget(self.btn_ok)

    def add_brow_img(self):  # выбор файла для Video Background
        try:
            path_image = QFileDialog.getOpenFileNames(self, caption="Open Image Team", directory="res")[0][0]
            self.line_image.setText(path_image)
        except IndexError:
            pass

    def add_ok(self):
        self.close()

    def add_cancel(self):
        self.close()


class MainRATING(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(200, 200)
        self.setMinimumSize(QtCore.QSize(200, 200))
        self.setMaximumSize(QtCore.QSize(200, 200))
        self.setStyleSheet("background-color: rgb(78, 79, 84);")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.centralwidget.setObjectName("centralwidget")

        self.btn_Add_Item = QtWidgets.QPushButton("Add Team", self.centralwidget)
        self.btn_Add_Item.setGeometry(QtCore.QRect(50, 85, 100, 30))
        self.btn_Add_Item.setFont(font)
        self.btn_Add_Item.setStyleSheet("color: rgb(209, 209, 217);")
        self.btn_Add_Item.setObjectName("btn_Add_Item")

        self.btn_Add_Item.clicked.connect(self.add_new_team)  # button "Add Item"

    def add_new_team(self):
        self.add_team = Add_Team()
        self.add_team.show()

        self.add_team.btn_brow_image.clicked.connect(self.add_team.add_brow_img)  # button "Browse..." Item Image

        self.add_team.btn_ok.clicked.connect(self.add_team.add_ok)  # button OK
        self.add_team.btn_ok.setAutoDefault(True)

        self.add_team.btn_cancel.clicked.connect(self.add_team.add_cancel)  # button CANCEL


def application():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    windows = MainRATING()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
