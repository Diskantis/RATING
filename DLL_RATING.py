# -*- coding: utf-8 -*-
import ast
import os
import re

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QLabel, QWidget

from UI_RATING import Ui_Preference, Ui_Add_Team, Ui_Widget_Team_Button, Ui_Widget_Team_Rating, Ui_Menu_Team


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


def team_widgets(list_str, layout):
    widgets = []
    for i in list_str[:len(list_str) + 1:]:
        index = str(layout.count() + 1)
        team = Widget_Team_Button(index, i[1])
        layout.addWidget(team)
        widgets.append(team)  # создаем список с виджетами команд
    return widgets


def team_widgets_rat(list_str, layout):
    widgets = []
    for i in enumerate(list_str[:len(list_str) + 1:]):

        team = Widget_Team_Rating(i[1][0])
        layout.addWidget(team, 0, QtCore.Qt.AlignHCenter)
        widgets.append(team)

        scale = i[1][2]
        pos_scale = i[1][3]

        pixmap = QPixmap(i[1][0])
        width = pixmap.width()

        pixmap = pixmap.scaledToWidth(int(width * pos_scale))
        team.image_team.setPixmap(pixmap)

        width = pixmap.width()
        height = pixmap.height()

        team.setFixedSize(QtCore.QSize(width, height))
        team.setFixedSize(QtCore.QSize(int(width * scale), int(height * scale)))

    return widgets


def read_reference(file_name):
    list_str = ""
    with open(file_name, "r") as f:
        for line in f.readlines():
            list_str += line.strip("\n")
    list_str = re.findall(r'"(.*?)"', list_str)

    def real_type(value):  # изменяет тип данных в зависимости от их типа (str -> bool, str -> int или float)
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value

    list_data = [real_type(i) for i in list_str]
    return list_data


def start_player():
    val = read_reference("reference.reg")
    if val[2]:
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        player_1 = VideoPlayer("Video Background", val[4])  # class dll.VideoPlayer
        return player_1, player_2
    elif val[3]:
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        player_1 = ImagePlayer("Image Background", val[5])  # class dll.ImagePlayer
        return player_1, player_2


class VideoPlayer:
    def __init__(self, name, path=None):
        self.video = QVideoWidget()
        self.video.setObjectName("VideoPlayer")
        self.video.setWindowTitle(name)
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        # self.video.move(1920, 0)
        # self.video.setFixedSize(1920, 1080)
        # self.video.setFullScreen(True)
        self.video.resize(749, 421)
        self.video.move(1100, 10)

        if path is not None:
            self.playlist = QMediaPlaylist()
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

            self.player = QMediaPlayer()
            self.player.setVideoOutput(self.video)
            self.player.setPlaylist(self.playlist)
            self.player.play()

        self.video.show()

    def pause(self):
        self.player.pause()

    def close(self):
        self.video.close()


class ImagePlayer:
    def __init__(self, name, path=None):

        self.video = QWidget()
        self.video.setObjectName("ImageRating")
        self.video.setWindowTitle(name)
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.video.setFixedSize(1920, 1080)
        # self.video.move(1920, 0)
        # self.video.resize(749, 421)
        # self.video.move(1100, 10)

        if path is None:
            self.video.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.video.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.video.activateWindow()

            # слой вертекального выравнивания группы виджетов команд
            self.v_Layout_grb_items_rat = QtWidgets.QVBoxLayout(self.video)
            self.v_Layout_grb_items_rat.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)  # SetDefaultConstraint
            self.v_Layout_grb_items_rat.setContentsMargins(0, 0, 0, 0)
            self.v_Layout_grb_items_rat.setSpacing(0)
            self.v_Layout_grb_items_rat.setObjectName("v_Layout_grb_items")

        if path is not None:
            # слой вертекального выравнивания Центрального виджета (всего окна)
            self.v_Layout_video = QtWidgets.QVBoxLayout(self.video)
            self.v_Layout_video.setContentsMargins(0, 0, 0, 0)
            self.v_Layout_video.setObjectName("v_Layout_video")

            self.image1 = QLabel()
            pixmap1 = QPixmap(path)
            pixmap1 = pixmap1.scaledToWidth(self.video.width())
            self.image1.setPixmap(pixmap1)
            self.v_Layout_video.addWidget(self.image1)

        self.video.show()

    def close(self):
        self.video.close()


class Preference(QtWidgets.QDialog, Ui_Preference):
    def __init__(self):
        super(Preference, self).__init__()

        self.setupUi(self)

    # TAB VIDEO
    def check_player_stat_chang(self):  # использовать внутрений видео плеер (Use internal video player)
        if self.check_box_player.checkState() == QtCore.Qt.Checked:
            print("check_player =", self.check_box_player.isTristate())
        elif self.check_box_player.checkState() == QtCore.Qt.Unchecked:
            print("check_player ", self.check_box_player.isTristate())

    def check_pause_stat_chang(self):  # во время анимации ставит видео на паузу (Pause playback when animating)
        if self.check_box_pause.checkState() == QtCore.Qt.Checked:
            print("check_pause True")
        elif self.check_box_pause.checkState() == QtCore.Qt.Unchecked:
            print("check_pause False")

    def bg_brow_vid(self):  # выбор файла для Video Background
        try:
            path_vid_1 = QFileDialog.getOpenFileNames(self, caption="Open Video Background", directory="res",
                                                      filter="*.avi *.mov")[0][0]

            self.line_back_video.setText(path_vid_1)
        except IndexError:
            pass

    def bg_brow_img(self):  # выбор файла для Image Background
        try:
            path_img = QFileDialog.getOpenFileNames(self, caption="Open Image Background", directory="res",
                                                    filter="*.jpg *.png")[0][0]
            self.line_back_image.setText(path_img)
        except IndexError:
            pass

    def lg_brow_vid(self):  # выбор файла для Video Logo
        try:
            path_vid_2 = QFileDialog.getOpenFileNames(self, caption="Open Video Logo", directory="res",
                                                      filter="*.avi *.mov")[0][0]
            self.line_logo_video.setText(path_vid_2)
        except IndexError:
            pass

    # TAB SCENE
    def margins(self, top, bottom):
        margins_team_rat = self.v_Layout_video.setContentsMargins(0, top, 0, bottom)
        return margins_team_rat

    def animation(self):
        pass

    # TAB COMMON
    def interface_lang(self):  # выбор языка интерфейса
        path = "lang"
        self.language = filter(lambda x: x.lower().endswith(('.qm',)), os.listdir(path))
        self.comboBox_language.addItems(self.language)

    # OK
    def save_preferences(self):
        with open("reference.reg", "w") as f:
            f.write(f'Use Internal Video Player = "{str(self.check_box_player.isChecked())}"\n')
            f.write(f'Pause Background When Animating = "{str(self.check_box_pause.isChecked())}"\n')
            f.write(f'Use Video Background = "{str(self.radio_btn_video_back.isChecked())}"\n')
            f.write(f'Use Image Background = "{str(self.radio_btn_image_back.isChecked())}"\n')
            f.write(f'Background Video File Name = "{str(self.line_back_video.displayText())}"\n')
            f.write(f'Background Image File Name = "{str(self.line_back_image.displayText())}"\n')
            f.write(f'Logo Video File Name = "{str(self.line_logo_video.displayText())}"\n')
            f.write(f'Margin Top = "{str(self.spin_box_top.value())}"\n')
            f.write(f'Margin Bottom = "{str(self.spin_box_bottom.value())}"\n')
            f.write(f'AnimationDuration = "{str(self.line_duration.displayText())}"\n')
            f.write(f'RestoreLastSession = "{str(self.check_last_session.isChecked())}"\n')
            f.write(f'Language = "{str(self.comboBox_language.currentText())}"\n')

    def pref_cancel(self):
        self.close()


class Add_Team(QtWidgets.QDialog, Ui_Add_Team):
    def __init__(self):
        super(Add_Team, self).__init__()

        self.setupUi(self)

    def add_team_brow_img(self):  # выбор файла для Video Background
        try:
            path_image = QFileDialog.getOpenFileNames(self, caption="Open Image Team", directory="res",
                                                      filter="*.jpg *.png")[0][0]
            self.line_image.setText(path_image)

        except IndexError:
            pass

    def add_cancel(self):
        self.close()


class Menu_Team(QtWidgets.QDialog, Ui_Menu_Team):
    def __init__(self):
        super(Menu_Team, self).__init__()

        self.setupUi(self)

    def menu_cancel(self):
        self.close()


class Position_Offset(Menu_Team):
    def __init__(self):
        super(Menu_Team, self).__init__()

        self.setupUi(self)

        self.resize(300, 170)
        self.setMinimumSize(QtCore.QSize(300, 170))
        self.setMaximumSize(QtCore.QSize(300, 170))
        self.setWindowTitle("Set position offset")
        self.grb_menu_parameter.setTitle("Position Offset")

        self.grb_menu_parameter.setGeometry(QtCore.QRect(10, 10, 280, 110))

        self.label_dX = self.label_parameter
        self.label_dX.setGeometry(QtCore.QRect(10, 30, 30, 30))
        self.label_dX.setText("dX:")

        self.line_dX = self.line_parameter
        self.line_dX.setGeometry(QtCore.QRect(35, 30, 232, 30))

        self.label_dY = QtWidgets.QLabel(self.grb_menu_parameter)
        self.label_dY.setGeometry(QtCore.QRect(10, 70, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dY.setFont(font)
        self.label_dY.setText("dY:")
        self.label_dY.setObjectName("label_text")

        self.line_dY = QtWidgets.QLineEdit(self.grb_menu_parameter)
        self.line_dY.setGeometry(QtCore.QRect(35, 70, 232, 30))
        self.line_dY.setFont(font)
        self.line_dY.setStyleSheet("border-radius: 4px; color: rgb(209, 209, 217); "
                                   "border: 1px solid rgba(50, 50, 50, 240); "
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255),"
                                   "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.line_dY.setObjectName("line_text")

        self.frame_ok.setGeometry(QtCore.QRect(0, 120, 300, 50))

    def menu_cancel(self):
        self.close()


class Widget_Team_Button(QtWidgets.QWidget, Ui_Widget_Team_Button):
    def __init__(self, index, name):
        super(Widget_Team_Button, self).__init__()

        self.setupUi(self)

        # # кнопка с названием команды
        self.btn_Team.setText(index)
        self.label_name_team.setText(name)


class Widget_Team_Rating(QtWidgets.QWidget, Ui_Widget_Team_Rating):
    def __init__(self, path):
        super(Widget_Team_Rating, self).__init__()

        self.setupUi(self)

        self.v_Layout_widget_team_rating = QtWidgets.QVBoxLayout(self)
        self.v_Layout_widget_team_rating.setContentsMargins(0, 0, 0, 0)
        self.v_Layout_widget_team_rating.setObjectName("v_Layout_widget_team_rating")

        self.pixmap = QPixmap(path)
        self.image_team.setPixmap(self.pixmap)
        self.v_Layout_widget_team_rating.addWidget(self.image_team)
