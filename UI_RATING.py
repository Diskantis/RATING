# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Главное окно приложения
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 660)
        MainWindow.setGeometry(QtCore.QRect(660, 240, 600, 660))
        MainWindow.setMinimumSize(QtCore.QSize(600, 660))
        MainWindow.setMaximumSize(QtCore.QSize(600, 16777215))
        MainWindow.setWindowIcon(QIcon('res/logo.png'))
        MainWindow.setStyleSheet("background-color: rgb(78, 79, 84);")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        # Центральный виджет (все окно)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # слой вертекального выравнивания Центрального виджета (всего окна)
        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 0, 10, 10)
        self.v_Layout_centralwidget.setObjectName("verticalLayout")

        # рамочка группы виджетов команд
        self.frame_grb_items_btn = QtWidgets.QFrame(self.centralwidget)
        self.frame_grb_items_btn.setMinimumSize(QtCore.QSize(580, 450))
        self.frame_grb_items_btn.setStyleSheet("QFrame {border-radius: 5px; "
                                               "border: 1px solid rgba(209, 209, 217, 240);}")
        self.frame_grb_items_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grb_items_btn.setObjectName("frame_items")

        # слой вертекального выравнивания группы виджетов команд
        self.v_Layout_grb_items_btn = QtWidgets.QVBoxLayout(self.frame_grb_items_btn)
        self.v_Layout_grb_items_btn.setObjectName("v_Layout_grb_items")

        # верхиний толкатель группы
        spacerItem_TOP = QtWidgets.QSpacerItem(20, 185, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_Layout_grb_items_btn.addItem(spacerItem_TOP)

        # виджеты команд
        self.frame_items = QtWidgets.QFrame(self.frame_grb_items_btn)
        self.frame_items.setMinimumSize(QtCore.QSize(560, 0))
        self.frame_items.setStyleSheet("QFrame {border: 0px solid;}")
        self.frame_items.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_items.setObjectName("frame_items")
        self.v_Layout_grb_items_btn.addWidget(self.frame_items)

        # слой вертекального выравнивания группы виджетов команд
        self.v_Layout_frame_items = QtWidgets.QVBoxLayout(self.frame_items)
        self.v_Layout_frame_items.setSpacing(10)
        self.v_Layout_frame_items.setContentsMargins(0, 0, 0, 0)
        self.v_Layout_frame_items.setObjectName("v_Layout_frame_items")

        # нижний толкатель группы
        spacerItem_BOT = QtWidgets.QSpacerItem(20, 185, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_Layout_grb_items_btn.addItem(spacerItem_BOT)

        # прикрепляет группу виджетов к слою центрального виджета
        self.v_Layout_centralwidget.addWidget(self.frame_grb_items_btn)

        # фрэйм с кнопками (Add Item, Remove Team, Swap Teams, Move to Position)
        self.frame_btn = QtWidgets.QFrame(self.centralwidget)
        self.frame_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_btn.setStyleSheet("QFrame {border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);}")
        self.frame_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn.setObjectName("frame_btn")

        # слой горизонтального выравнивания фрэйма с кнопками
        self.h_Layout_frame_btn = QtWidgets.QHBoxLayout(self.frame_btn)
        self.h_Layout_frame_btn.setObjectName("h_Layout_frame_btn")

        # кнопка добавления команды
        self.btn_Add_Team = QtWidgets.QPushButton(self.frame_btn)
        self.btn_Add_Team.setGeometry(QtCore.QRect(0, 480, 100, 30))
        self.btn_Add_Team.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_Add_Team.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_Add_Team.setFont(font)
        self.btn_Add_Team.setStyleSheet("color: rgb(209, 209, 217);")
        self.btn_Add_Team.setObjectName("btn_Add_Item")
        self.h_Layout_frame_btn.addWidget(self.btn_Add_Team)

        # кнопка удаления команды
        self.btn_Remove_Team = QtWidgets.QPushButton(self.frame_btn)
        self.btn_Remove_Team.setEnabled(False)
        self.btn_Remove_Team.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_Remove_Team.setMaximumSize(QtCore.QSize(120, 30))
        self.btn_Remove_Team.setFont(font)
        self.btn_Remove_Team.setStyleSheet(":enabled { color: rgb(209, 209, 217);}"
                                           ":disabled { color: rgba(209, 209, 217, 100);}")
        self.btn_Remove_Team.setObjectName("btn_Remove_Item")
        self.h_Layout_frame_btn.addWidget(self.btn_Remove_Team)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_frame_btn.addItem(spacerItem)

        # кнопка взаимного перемещения команд
        self.btn_Swap_Teams = QtWidgets.QPushButton(self.frame_btn)
        self.btn_Swap_Teams.setEnabled(False)
        self.btn_Swap_Teams.setMinimumSize(QtCore.QSize(110, 30))
        self.btn_Swap_Teams.setMaximumSize(QtCore.QSize(110, 30))
        self.btn_Swap_Teams.setFont(font)
        self.btn_Swap_Teams.setStyleSheet(":enabled { color: rgb(209, 209, 217);}"
                                          ":disabled { color: rgba(209, 209, 217, 100);}")
        self.btn_Swap_Teams.setObjectName("btn_Swap_Items")
        self.h_Layout_frame_btn.addWidget(self.btn_Swap_Teams)

        # кнопка перемещения команды на позицию
        self.btn_Move_to_Pos = QtWidgets.QPushButton(self.frame_btn)
        self.btn_Move_to_Pos.setEnabled(False)
        self.btn_Move_to_Pos.setGeometry(QtCore.QRect(380, 480, 160, 30))
        self.btn_Move_to_Pos.setMinimumSize(QtCore.QSize(160, 30))
        self.btn_Move_to_Pos.setMaximumSize(QtCore.QSize(160, 30))
        self.btn_Move_to_Pos.setFont(font)
        self.btn_Move_to_Pos.setStyleSheet(":enabled { color: rgb(209, 209, 217);}"
                                           ":disabled { color: rgba(209, 209, 217, 100);}")
        self.btn_Move_to_Pos.setObjectName("btn_Move_to_Pos")
        self.h_Layout_frame_btn.addWidget(self.btn_Move_to_Pos)

        # окошко с номером позиции на которую должна переместиться команда
        self.lineEdit_Pos = QtWidgets.QLineEdit(self.frame_btn)
        self.lineEdit_Pos.setGeometry(QtCore.QRect(550, 480, 40, 30))
        self.lineEdit_Pos.setMinimumSize(QtCore.QSize(40, 30))
        self.lineEdit_Pos.setMaximumSize(QtCore.QSize(40, 30))
        font_l = QtGui.QFont()
        font_l.setPointSize(12)
        font_l.setWeight(75)
        self.lineEdit_Pos.setMaxLength(2)
        self.lineEdit_Pos.setFont(font_l)
        self.lineEdit_Pos.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                        "border: 1px solid rgba(50, 50, 50, 240); "
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                        "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                        "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_Pos.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Pos.setObjectName("lineEdit")
        self.h_Layout_frame_btn.addWidget(self.lineEdit_Pos)

        self.v_Layout_centralwidget.addWidget(self.frame_btn)

        # кнопка переключения между ЛОГО и РЕЙТИНГОМ
        self.btn_Logo_Rating = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logo_Rating.setGeometry(QtCore.QRect(10, 520, 580, 40))
        self.btn_Logo_Rating.setMinimumSize(QtCore.QSize(580, 40))
        self.btn_Logo_Rating.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_Logo_Rating.setFont(font)
        self.btn_Logo_Rating.setCheckable(True)
        self.btn_Logo_Rating.setStyleSheet("QPushButton {color: rgb(209, 209, 217);}"
                                           "QPushButton:checked {border-radius: 4px; color: rgb(209, 209, 217); "
                                           "border: 1px solid rgba(50, 50, 50, 240); "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                           "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255))}")
        self.btn_Logo_Rating.setObjectName("pushButton")
        self.v_Layout_centralwidget.addWidget(self.btn_Logo_Rating)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(10, 10, 800, 20))
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color: rgb(209, 209, 217); padding: .5em;")
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setFont(font)
        self.menuFile.setStyleSheet("border-bottom: 0px; selection-color: rgb(0, 0, 0); color: rgb(209, 209, 217);")
        self.menuFile.setObjectName("menuFile")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setFont(font)
        self.menuOptions.setStyleSheet("border-bottom: 0px; selection-color: rgb(0, 0, 0); color: rgb(209, 209, 217);")
        self.menuOptions.setObjectName("menuOptions")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setFont(font)
        self.menuHelp.setStyleSheet("border-bottom: 0px; selection-color: rgb(0, 0, 0); color: rgb(209, 209, 217);")
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)

        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setObjectName("actionNew")

        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("actionOpen")

        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("actionSave")

        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("actionExit")

        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setObjectName("actionPreferences")

        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("actionAbout")

        self.menuFile.addAction(self.action_New)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)

        self.menuOptions.addAction(self.action_Preferences)

        self.menuHelp.addAction(self.action_About)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 'TEAM RANKING "WHAT? WHERE? WHEN?"'))
        self.btn_Add_Team.setText(_translate("MainWindow", "Add Team", ))
        self.btn_Remove_Team.setText(_translate("MainWindow", "Remove Team"))
        self.btn_Swap_Teams.setText(_translate("MainWindow", "Swap Teams"))
        self.btn_Move_to_Pos.setText(_translate("MainWindow", "Move to Position №"))
        self.btn_Logo_Rating.setText(_translate("MainWindow", "L O G O / R A T I N G"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        self.action_New.setText(_translate("MainWindow", "New"))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.action_Open.setText(_translate("MainWindow", "Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+L"))

        self.action_Save.setText(_translate("MainWindow", "Save"))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.action_Exit.setText(_translate("MainWindow", "Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+E"))

        self.action_Preferences.setText(_translate("MainWindow", "Preferences"))
        self.action_Preferences.setShortcut(_translate("MainWindow", "Ctrl+P"))

        self.action_About.setText(_translate("MainWindow", "About"))
        self.action_About.setShortcut(_translate("MainWindow", "Ctrl+A"))


class Ui_Preference(object):
    def setupUi(self, Preference):
        Preference.setObjectName("Preference")
        Preference.setWindowModality(QtCore.Qt.ApplicationModal)
        Preference.resize(400, 440)
        Preference.setMinimumSize(QtCore.QSize(400, 440))
        Preference.setMaximumSize(QtCore.QSize(400, 440))
        Preference.setStyleSheet("background-color: rgb(78, 79, 84); color: rgb(209, 209, 217);")

        font = QtGui.QFont()
        font.setPointSize(10)

        self.tab_Widget = QtWidgets.QTabWidget(Preference)
        self.tab_Widget.setGeometry(QtCore.QRect(10, 10, 380, 380))
        self.tab_Widget.setFont(font)
        self.tab_Widget.setObjectName("tab_Widget")

        # TAB VIDEO
        self.tab_Video = QtWidgets.QWidget()
        self.tab_Video.setObjectName("tab_Video")

        self.grp_background = QtWidgets.QGroupBox(self.tab_Video)
        self.grp_background.setGeometry(QtCore.QRect(10, 10, 355, 230))
        font_grp = QtGui.QFont()
        font_grp.setPointSize(10)
        font_grp.setBold(True)
        font_grp.setUnderline(True)
        self.grp_background.setFont(font_grp)
        self.grp_background.setStyleSheet("border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);")
        self.grp_background.setAlignment(QtCore.Qt.AlignCenter)
        self.grp_background.setObjectName("grp_background")

        self.check_box_player = QtWidgets.QCheckBox(self.grp_background)
        self.check_box_player.setGeometry(QtCore.QRect(12, 20, 330, 30))
        self.check_box_player.setFont(font)
        self.check_box_player.setChecked(False)
        self.check_box_player.setStyleSheet("border: 0px solid;")
        self.check_box_player.setObjectName("check_box_player")

        self.check_box_pause = QtWidgets.QCheckBox(self.grp_background)
        self.check_box_pause.setGeometry(QtCore.QRect(12, 50, 330, 30))
        self.check_box_pause.setFont(font)
        self.check_box_pause.setChecked(False)
        self.check_box_pause.setStyleSheet("border: 0px solid;")
        self.check_box_pause.setObjectName("check_box_pause")

        self.frame_back_video = QtWidgets.QFrame(self.tab_Video)
        self.frame_back_video.setGeometry(QtCore.QRect(12, 118, 350, 50))
        self.frame_back_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_back_video.setObjectName("frame_back_video")

        self.h_Layout_back_video = QtWidgets.QHBoxLayout(self.frame_back_video)
        self.h_Layout_back_video.setObjectName("h_Layout_back_video")

        self.line_back_video = QtWidgets.QLineEdit(self.frame_back_video)
        self.line_back_video.setMinimumSize(QtCore.QSize(0, 30))
        self.line_back_video.setFont(font)
        self.line_back_video.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                           "border: 1px solid rgba(50, 50, 50, 240); "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                           "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_back_video.setObjectName("line_back_video")
        self.h_Layout_back_video.addWidget(self.line_back_video)

        self.btn_bg_brow_vid = QtWidgets.QPushButton(self.frame_back_video)
        self.btn_bg_brow_vid.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_bg_brow_vid.setFont(font)
        self.btn_bg_brow_vid.setObjectName("btn_bg_brow_vid")
        self.h_Layout_back_video.addWidget(self.btn_bg_brow_vid)

        self.radio_btn_video_back = QtWidgets.QRadioButton(self.grp_background)
        self.radio_btn_video_back.setChecked(True)
        self.radio_btn_video_back.setGeometry(QtCore.QRect(12, 85, 330, 30))
        self.radio_btn_video_back.setFont(font)
        self.radio_btn_video_back.setStyleSheet("border: 0px solid;")
        self.radio_btn_video_back.setObjectName("radio_btn_video_back")

        self.frame_back_image = QtWidgets.QFrame(self.tab_Video)
        self.frame_back_image.setGeometry(QtCore.QRect(12, 188, 350, 50))
        self.frame_back_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_back_image.setObjectName("frame_back_image")

        self.h_Layout_back_image = QtWidgets.QHBoxLayout(self.frame_back_image)
        self.h_Layout_back_image.setObjectName("h_Layout_back_image")

        self.line_back_image = QtWidgets.QLineEdit(self.frame_back_image)
        self.line_back_image.setMinimumSize(QtCore.QSize(0, 30))
        self.line_back_image.setFont(font)
        self.line_back_image.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                           "border: 1px solid rgba(50, 50, 50, 240); "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                           "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_back_image.setObjectName("line_back_image")
        self.h_Layout_back_image.addWidget(self.line_back_image)

        self.btn_bg_brow_img = QtWidgets.QPushButton(self.frame_back_image)
        self.btn_bg_brow_img.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_bg_brow_img.setFont(font)
        self.btn_bg_brow_img.setObjectName("btn_bg_brow_img")
        self.h_Layout_back_image.addWidget(self.btn_bg_brow_img)

        self.radio_btn_image_back = QtWidgets.QRadioButton(self.grp_background)
        self.radio_btn_image_back.setChecked(False)
        self.radio_btn_image_back.setGeometry(QtCore.QRect(12, 155, 330, 30))
        self.radio_btn_image_back.setFont(font)
        self.radio_btn_image_back.setStyleSheet("border: 0px solid;")
        self.radio_btn_image_back.setObjectName("radio_btn_image_back")

        self.grp_logo = QtWidgets.QGroupBox(self.tab_Video)
        self.grp_logo.setGeometry(QtCore.QRect(10, 250, 355, 90))
        self.grp_logo.setFont(font_grp)
        self.grp_logo.setStyleSheet("border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);")
        self.grp_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.grp_logo.setObjectName("grp_logo")

        self.frame_logo_video = QtWidgets.QFrame(self.tab_Video)
        self.frame_logo_video.setGeometry(QtCore.QRect(12, 288, 350, 50))
        self.frame_logo_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo_video.setObjectName("frame_video_logo")

        self.h_Layout_video_logo = QtWidgets.QHBoxLayout(self.frame_logo_video)
        self.h_Layout_video_logo.setObjectName("h_Layout_video_logo")

        self.line_logo_video = QtWidgets.QLineEdit(self.frame_logo_video)
        self.line_logo_video.setMinimumSize(QtCore.QSize(0, 30))
        self.line_logo_video.setFont(font)
        self.line_logo_video.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                           "border: 1px solid rgba(50, 50, 50, 240); "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                           "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_logo_video.setObjectName("line_video_logo")
        self.h_Layout_video_logo.addWidget(self.line_logo_video)

        self.btn_lg_brow_vid = QtWidgets.QPushButton(self.frame_logo_video)
        self.btn_lg_brow_vid.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_lg_brow_vid.setFont(font)
        self.btn_lg_brow_vid.setObjectName("btn_lg_brow_vid")
        self.h_Layout_video_logo.addWidget(self.btn_lg_brow_vid)

        self.label_logo_video = QtWidgets.QLabel(self.grp_logo)
        self.label_logo_video.setGeometry(QtCore.QRect(12, 15, 330, 30))
        self.label_logo_video.setFont(font)
        self.label_logo_video.setStyleSheet("border: 0px solid;")
        self.label_logo_video.setObjectName("label_video_logo")

        self.tab_Widget.addTab(self.tab_Video, "")

        # TAB RATING
        self.tab_Scene = QtWidgets.QWidget()
        self.tab_Scene.setObjectName("tab_Scene")

        self.grp_margins = QtWidgets.QGroupBox(self.tab_Scene)
        self.grp_margins.setGeometry(QtCore.QRect(10, 10, 355, 113))
        self.grp_margins.setFont(font_grp)
        self.grp_margins.setStyleSheet("border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);")
        self.grp_margins.setAlignment(QtCore.Qt.AlignCenter)
        self.grp_margins.setObjectName("grp_margins")

        self.label_top = QtWidgets.QLabel(self.grp_margins)
        self.label_top.setGeometry(QtCore.QRect(12, 30, 50, 30))
        self.label_top.setFont(font)
        self.label_top.setStyleSheet("border: 0px solid;")
        self.label_top.setObjectName("label_top")

        self.label_bottom = QtWidgets.QLabel(self.grp_margins)
        self.label_bottom.setGeometry(QtCore.QRect(12, 70, 50, 30))
        self.label_bottom.setFont(font)
        self.label_bottom.setStyleSheet("border: 0px solid;")
        self.label_bottom.setObjectName("label_bottom")

        self.spin_box_top = QtWidgets.QSpinBox(self.grp_margins)
        self.spin_box_top.setGeometry(QtCore.QRect(65, 30, 278, 30))
        self.spin_box_top.setDisplayIntegerBase(10)
        self.spin_box_top.setMaximum(999)
        self.spin_box_top.setFont(font)
        self.spin_box_top.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                        "border: 1px solid rgba(50, 50, 50, 240); "
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                        "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                        "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.spin_box_top.setObjectName("spin_box_top")

        self.spin_box_bottom = QtWidgets.QSpinBox(self.grp_margins)
        self.spin_box_bottom.setGeometry(QtCore.QRect(65, 70, 278, 30))
        self.spin_box_bottom.setDisplayIntegerBase(10)
        self.spin_box_bottom.setMaximum(999)
        self.spin_box_bottom.setFont(font)
        self.spin_box_bottom.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                           "border: 1px solid rgba(50, 50, 50, 240); "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                           "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.spin_box_bottom.setObjectName("spin_box_bottom")

        self.grp_animation = QtWidgets.QGroupBox(self.tab_Scene)
        self.grp_animation.setGeometry(QtCore.QRect(10, 133, 355, 73))
        self.grp_animation.setFont(font_grp)
        self.grp_animation.setStyleSheet("border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);")
        self.grp_animation.setAlignment(QtCore.Qt.AlignCenter)
        self.grp_animation.setObjectName("grp_animation")

        self.label_duration = QtWidgets.QLabel(self.grp_animation)
        self.label_duration.setGeometry(QtCore.QRect(12, 30, 130, 30))
        self.label_duration.setFont(font)
        self.label_duration.setStyleSheet("border: 0px solid;")
        self.label_duration.setObjectName("label_duration")

        self.line_duration = QtWidgets.QLineEdit(self.grp_animation)
        self.line_duration.setGeometry(QtCore.QRect(140, 30, 203, 30))  # 115
        self.line_duration.setFont(font)
        self.line_duration.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                         "border: 1px solid rgba(50, 50, 50, 240); "
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                         "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                         "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_duration.setObjectName("line_duration")

        self.tab_Widget.addTab(self.tab_Scene, "")

        # TAB COMMON
        self.tab_Common = QtWidgets.QWidget()
        self.tab_Common.setObjectName("tab_Common")

        self.check_last_session = QtWidgets.QCheckBox(self.tab_Common)
        self.check_last_session.setGeometry(QtCore.QRect(12, 10, 330, 30))
        self.check_last_session.setFont(font)
        self.check_last_session.setChecked(True)
        self.check_last_session.setObjectName("check_last_session")

        self.label_interface_language = QtWidgets.QLabel(self.tab_Common)
        self.label_interface_language.setGeometry(QtCore.QRect(12, 40, 260, 30))
        self.label_interface_language.setFont(font)
        self.label_interface_language.setObjectName("label_interface_language")

        self.label_restart_for_changing = QtWidgets.QLabel(self.tab_Common)
        self.label_restart_for_changing.setGeometry(QtCore.QRect(12, 95, 330, 30))
        font_restart = QtGui.QFont()
        font_restart.setPointSize(8)
        self.label_restart_for_changing.setFont(font_restart)
        self.label_restart_for_changing.setObjectName("label_restart_for_changing")

        self.comboBox_language = QtWidgets.QComboBox(self.tab_Common)
        self.comboBox_language.setGeometry(QtCore.QRect(12, 70, 350, 30))
        self.comboBox_language.setFont(font)
        self.comboBox_language.setObjectName("comboBox_language")

        self.tab_Widget.addTab(self.tab_Common, "")

        # FRAME OK
        self.frame_ok = QtWidgets.QFrame(Preference)
        self.frame_ok.setEnabled(True)
        self.frame_ok.setGeometry(QtCore.QRect(10, 390, 388, 50))
        self.frame_ok.setMinimumSize(QtCore.QSize(388, 50))
        self.frame_ok.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_ok.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ok.setLineWidth(0)
        self.frame_ok.setObjectName("frame_ok")

        self.h_Layout_ok = QtWidgets.QHBoxLayout(self.frame_ok)
        self.h_Layout_ok.setObjectName("h_Layout_ok")

        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_ok.addItem(spacerItem1)

        self.btn_cancel = QtWidgets.QPushButton(self.frame_ok)
        self.btn_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_Layout_ok.addWidget(self.btn_cancel)

        self.btn_ok = QtWidgets.QPushButton(self.frame_ok)
        self.btn_ok.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.h_Layout_ok.addWidget(self.btn_ok)

        self.retranslateUi(Preference)
        QtCore.QMetaObject.connectSlotsByName(Preference)

    def retranslateUi(self, Preference):
        _translate = QtCore.QCoreApplication.translate
        Preference.setWindowTitle(_translate("Preference", "Preference"))
        self.grp_background.setTitle(_translate("Preference", "Background:"))
        self.btn_bg_brow_vid.setText(_translate("Preference", "Browse..."))
        self.check_box_player.setText(_translate("Preference", "Use internal video player"))
        self.check_box_pause.setText(_translate("Preference", "Pause playback when animating"))
        self.btn_bg_brow_img.setText(_translate("Preference", "Browse..."))
        self.radio_btn_video_back.setText(_translate("Preference", "Video file:"))
        self.radio_btn_image_back.setText(_translate("Preference", "Image file:"))
        self.grp_logo.setTitle(_translate("Preference", "Logo:"))
        self.btn_lg_brow_vid.setText(_translate("Preference", "Browse..."))
        self.label_logo_video.setText(_translate("Preference", "Video file:"))
        self.tab_Widget.setTabText(self.tab_Widget.indexOf(self.tab_Video), _translate("Preference", "Video"))
        self.grp_margins.setTitle(_translate("Preference", "Margins:"))
        self.label_top.setText(_translate("Preference", "Top:"))
        self.label_bottom.setText(_translate("Preference", "Bottom:"))
        self.grp_animation.setTitle(_translate("Preference", "Animation:"))
        self.label_duration.setText(_translate("Preference", "Duration, msecs:"))
        self.tab_Widget.setTabText(self.tab_Widget.indexOf(self.tab_Scene), _translate("Preference", "Rating"))
        self.check_last_session.setText(_translate("Preference", "Restore last session"))
        self.label_interface_language.setText(_translate("Preference", "Interface language:*"))
        self.label_restart_for_changing.setText(_translate(
            "Preference", "* - Changing this setting requires restarting of the application"))
        self.tab_Widget.setTabText(self.tab_Widget.indexOf(self.tab_Common), _translate("Preference", "Common"))
        self.btn_cancel.setText(_translate("Preference", "Cancel"))
        self.btn_ok.setText(_translate("Preference", "OK"))


class Ui_About(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self):
        self.setObjectName("About")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(290, 170)
        self.setStyleSheet("background-color: rgb(78, 79, 84);")
        self.setWindowTitle("About")

        self.label_scene = QtWidgets.QLabel(self)
        self.label_scene.setGeometry(QtCore.QRect(10, 5, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_scene.setFont(font)
        self.label_scene.setStyleSheet("font-weight: 700; color: rgb(209, 209, 217); padding: 5px 0 5px 0;")
        self.label_scene.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scene.setObjectName("label_scene")

        self.label_release = QtWidgets.QLabel(self)
        self.label_release.setGeometry(QtCore.QRect(10, 35, 270, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_release.setFont(font)
        self.label_release.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: 5px 0 5px 0;")
        self.label_release.setAlignment(QtCore.Qt.AlignCenter)
        self.label_release.setObjectName("label_release")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("About", "About"))
        self.label_scene.setText(_translate("About", "RATING"))
        self.label_release.setText(_translate("About", "Release 1.1 \n\n Author - Sergey Litvinov \n linch@adsl.by \n\n"
                                                       " Python adaptation - Michael Zajkov \n mn.zajkov@gmail.com"))


class Ui_Add_Team(object):
    def setupUi(self, Add_team):
        Add_team.setObjectName("Add_team")
        Add_team.setWindowModality(QtCore.Qt.ApplicationModal)
        Add_team.resize(400, 210)
        Add_team.setMinimumSize(QtCore.QSize(400, 210))
        Add_team.setMaximumSize(QtCore.QSize(400, 210))
        Add_team.setStyleSheet("background-color: rgb(78, 79, 84); color: rgb(209, 209, 217);")

        font = QtGui.QFont()
        font.setPointSize(10)

        self.grb_team_prp = QtWidgets.QGroupBox(Add_team)
        self.grb_team_prp.setGeometry(QtCore.QRect(10, 10, 380, 150))
        font_grp = QtGui.QFont()
        font_grp.setPointSize(10)
        font_grp.setBold(True)
        font_grp.setUnderline(True)
        self.grb_team_prp.setFont(font_grp)
        self.grb_team_prp.setStyleSheet("QGroupBox {border-radius: 5px; border: 1px solid rgba(209, 209, 217, 240);} ")
        self.grb_team_prp.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_team_prp.setObjectName("grb_team_prp")

        self.frame_image = QtWidgets.QFrame(self.grb_team_prp)
        self.frame_image.setGeometry(QtCore.QRect(1, 40, 378, 50))
        self.frame_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_image.setObjectName("frame_image")

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
        self.line_image.setObjectName("line_image")
        self.h_Layout_frame_image.addWidget(self.line_image)

        self.btn_brow_image = QtWidgets.QPushButton(self.frame_image)
        self.btn_brow_image.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_brow_image.setFont(font)
        self.btn_brow_image.setObjectName("btn_brow_image")
        self.h_Layout_frame_image.addWidget(self.btn_brow_image)

        self.label_image = QtWidgets.QLabel(self.grb_team_prp)
        self.label_image.setGeometry(QtCore.QRect(12, 20, 355, 30))
        self.label_image.setFont(font)
        self.label_image.setObjectName("label_image")

        self.label_text = QtWidgets.QLabel(self.grb_team_prp)
        self.label_text.setGeometry(QtCore.QRect(12, 80, 355, 30))
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")

        self.line_text = QtWidgets.QLineEdit(self.grb_team_prp)
        self.line_text.setGeometry(QtCore.QRect(12, 110, 355, 30))
        self.line_text.setFont(font)
        self.line_text.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                     "border: 1px solid rgba(50, 50, 50, 240); "
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                     "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                     "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_text.setObjectName("line_text")

        # FRAME OK ADD_NEW_ITEM
        self.frame_ok = QtWidgets.QFrame(Add_team)
        self.frame_ok.setEnabled(True)
        self.frame_ok.setGeometry(QtCore.QRect(0, 160, 400, 50))
        self.frame_ok.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ok.setObjectName("frame_ok")

        self.h_Layout_ok = QtWidgets.QHBoxLayout(self.frame_ok)
        self.h_Layout_ok.setObjectName("h_Layout_ok")

        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_ok.addItem(spacerItem1)

        self.btn_cancel = QtWidgets.QPushButton(self.frame_ok)
        self.btn_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_Layout_ok.addWidget(self.btn_cancel)

        self.btn_ok = QtWidgets.QPushButton(self.frame_ok)
        self.btn_ok.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.h_Layout_ok.addWidget(self.btn_ok)

        self.retranslateUi(Add_team)
        QtCore.QMetaObject.connectSlotsByName(Add_team)

    def retranslateUi(self, Add_team):
        _translate = QtCore.QCoreApplication.translate
        Add_team.setWindowTitle(_translate("Add_team", "Add new Team"))
        self.grb_team_prp.setTitle(_translate("Add_team", "Team properties:"))
        self.label_image.setText(_translate("Add_team", "Image:"))
        self.label_text.setText(_translate("Add_team", "Text:"))
        self.btn_brow_image.setText(_translate("Add_team", "Browse..."))

        self.btn_cancel.setText(_translate("Add_team", "Cancel"))
        self.btn_ok.setText(_translate("Add_team", "OK"))


class Ui_Menu_Team(object):
    def setupUi(self, Menu_Team):
        Menu_Team.setObjectName("Item_scale")
        Menu_Team.setWindowModality(QtCore.Qt.ApplicationModal)
        Menu_Team.resize(300, 150)
        Menu_Team.setMinimumSize(QtCore.QSize(300, 150))
        Menu_Team.setMaximumSize(QtCore.QSize(300, 150))
        Menu_Team.setStyleSheet("background-color: rgb(78, 79, 84); color: rgb(209, 209, 217);")

        font = QtGui.QFont()
        font.setPointSize(10)

        self.grb_menu_parameter = QtWidgets.QGroupBox(Menu_Team)
        self.grb_menu_parameter.setGeometry(QtCore.QRect(10, 10, 280, 90))
        font_grp = QtGui.QFont()
        font_grp.setPointSize(10)
        font_grp.setBold(True)
        font_grp.setUnderline(True)
        self.grb_menu_parameter.setFont(font_grp)
        self.grb_menu_parameter.setStyleSheet("QGroupBox {border-radius: 5px; "
                                              "border: 1px solid rgba(209, 209, 217, 240);}")
        self.grb_menu_parameter.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_menu_parameter.setObjectName("grb_team_prp")

        self.label_parameter = QtWidgets.QLabel(self.grb_menu_parameter)
        self.label_parameter.setGeometry(QtCore.QRect(12, 20, 255, 30))
        self.label_parameter.setFont(font)
        self.label_parameter.setObjectName("label_text")

        self.line_parameter = QtWidgets.QLineEdit(self.grb_menu_parameter)
        self.line_parameter.setGeometry(QtCore.QRect(12, 50, 255, 30))
        self.line_parameter.setFont(font)
        self.line_parameter.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                          "border: 1px solid rgba(50, 50, 50, 240); "
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                          "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                          "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_parameter.setObjectName("line_text")

        # FRAME OK ADD_NEW_ITEM
        self.frame_ok = QtWidgets.QFrame(Menu_Team)
        self.frame_ok.setEnabled(True)
        self.frame_ok.setGeometry(QtCore.QRect(0, 100, 300, 50))
        self.frame_ok.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ok.setObjectName("frame_ok")

        self.h_Layout_ok = QtWidgets.QHBoxLayout(self.frame_ok)
        self.h_Layout_ok.setObjectName("h_Layout_ok")

        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_ok.addItem(spacerItem1)

        self.btn_cancel = QtWidgets.QPushButton(self.frame_ok)
        self.btn_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_Layout_ok.addWidget(self.btn_cancel)

        self.btn_ok = QtWidgets.QPushButton(self.frame_ok)
        self.btn_ok.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.h_Layout_ok.addWidget(self.btn_ok)

        self.retranslateUi(Menu_Team)
        QtCore.QMetaObject.connectSlotsByName(Menu_Team)
        Menu_Team.setTabOrder(self.btn_ok, self.btn_cancel)

    def retranslateUi(self, Menu_Team):
        _translate = QtCore.QCoreApplication.translate
        Menu_Team.setWindowTitle(_translate("Menu_Team", "Set scale"))
        self.grb_menu_parameter.setTitle(_translate("Menu_Team", "Item Scale"))
        self.label_parameter.setText(_translate("Menu_Team", "Enter scale:"))

        self.btn_cancel.setText(_translate("Menu_Team", "Cancel"))
        self.btn_ok.setText(_translate("Menu_Team", "OK"))


class Ui_Widget_Team_Button(object):
    def setupUi(self, Widget_Team):
        # слой вертекального выравнивания виджета команды
        self.v_Layout_widget_Team = QtWidgets.QVBoxLayout(Widget_Team)
        self.v_Layout_widget_Team.setContentsMargins(0, 0, 0, 0)
        self.v_Layout_widget_Team.setObjectName("v_Layout_widget_Team")

        # кнопка с названием команды
        self.btn_Team = QtWidgets.QPushButton(Widget_Team)
        self.btn_Team.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_Team.setFont(font)
        self.btn_Team.isChecked()
        self.btn_Team.setCheckable(True)
        self.btn_Team.setStyleSheet("QPushButton {color: rgb(0, 0, 190); text-align: left; padding: 0 0 0 2em ;} "
                                    "QPushButton:checked {border-radius: 4px; color: rgb(244, 202, 22); "
                                    "border: 1px solid rgba(50, 50, 50, 240); "
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                    "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                    "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255))}")
        self.btn_Team.setObjectName("btn_Team")
        self.btn_Team.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.v_Layout_widget_Team.addWidget(self.btn_Team)

        self.label_name_team = QtWidgets.QLabel(self.btn_Team)
        self.label_name_team.setGeometry(QtCore.QRect(0, 0, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_name_team.setFont(font)
        self.label_name_team.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(209, 209, 217);")
        self.label_name_team.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_team.setObjectName("label_name_team")
        # self.v_Layout_widget_Team.addWidget(self.btn_Team)

        self.menuTeam = QtWidgets.QMenu(Widget_Team)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuTeam.setFont(font)
        self.menuTeam.setStyleSheet("border-bottom: 0px; selection-color: rgb(0, 0, 0); color: rgb(209, 209, 217);")

        _translate = QtCore.QCoreApplication.translate
        self.edt_team = self.menuTeam.addAction(_translate("menuTeam", "Edit"))
        self.menuTeam.addSeparator()
        self.itm_scale = self.menuTeam.addAction(_translate("menuTeam", "Set item scale"))
        self.pos_scale = self.menuTeam.addAction(_translate("menuTeam", "Set position scale"))
        self.pos_offset = self.menuTeam.addAction(_translate("menuTeam", "Set position offset"))
        self.menuTeam.addSeparator()
        self.rem_team = self.menuTeam.addAction(_translate("menuTeam", "Remove"))
