import ast
import os
import re
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl, Qt, QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QLabel, QHBoxLayout, QWidget

from UI_RATING import Ui_Preference, Ui_Add_Item


def read_reference(file_name):
    list_str = ""
    with open(file_name, "r") as f:
        for line in f.readlines():
            list_str += line.strip("\n")
    list_str = re.findall(r'"(.*?)"', list_str)

    def real_type(value):  # изменяет тип данных в зависимости от их типа (str -> bool, str -> int или float)
        try:
            return ast.literal_eval(value)
        except:
            return value

    list_data = [real_type(i) for i in list_str]
    return list_data


def start_player():
    val = read_reference("reference.reg")

    # if val[4] and val[6]:

    if val[2]:
        player_1 = VideoPlayer("Video Background", val[4])  # class dll.VideoPlayer
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        return player_1, player_2

    elif val[3]:
        player_1 = ImagePlayer("Image Background", val[5])
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        return player_1, player_2


class VideoPlayer:
    def __init__(self, name, path):
        self.video = QVideoWidget()
        self.video.setWindowTitle(name)
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        # self.video.move(1920, 0)
        # self.video.setFixedSize(1920, 1080)
        # self.video.setFullScreen(True)
        self.video.move(10, 10)
        self.video.setFixedSize(800, 600)

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def close(self):
        self.video.close()


class ImagePlayer:
    def __init__(self, name, path):
        self.video = QWidget()
        self.video.setWindowTitle(name)
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        # self.video.move(1920, 0)
        # self.video.resize(1920, 1080)
        self.video.move(10, 10)
        self.video.resize(800, 600)

        self.image1 = QLabel()
        layout_box = QHBoxLayout(self.video)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.image1)

        pixmap1 = QPixmap(path)
        self.image1.setPixmap(pixmap1)
        # pixmap1 = pixmap1.scaledToWidth(self.image_wid.width())

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
        path_vid_1 = QFileDialog.getOpenFileNames(caption="Open Video Background",
                                                  directory="res",
                                                  filter="*.avi *.mov")[0][0]
        try:
            self.line_back_video.setText(path_vid_1)
        except IndexError:
            pass

    def bg_brow_img(self):  # выбор файла для Image Background
        path_img = QFileDialog.getOpenFileNames(caption="Open Image Background",
                                                directory="res",
                                                filter="*.jpg *.png")[0][0]
        try:
            self.line_back_image.setText(path_img)
        except IndexError:
            pass

    def lg_brow_vid(self):  # выбор файла для Video Logo
        path_vid_2 = QFileDialog.getOpenFileNames(caption="Open Video Logo",
                                                  directory="res",
                                                  filter="*.avi *.mov")[0][0]
        try:
            self.line_logo_video.setText(path_vid_2)
        except IndexError:
            pass

    # TAB SCENE
    def margins(self):
        pass

    def animation(self):
        pass

    # TAB COMMON
    def last_session(self):
        pass

    def interface_lang(self):  # выбор языка интерфейса
        path = "lang"
        self.language = filter(lambda x: x.lower().endswith(('.qm',)), os.listdir(path))
        self.comboBox_language.addItems(self.language)

    # OK
    def save_preferences(self):
        with open("reference.reg", "w") as f:
            print("Use Internal Video Player", "=", '"' + str(self.check_box_player.isChecked()) + '"', file=f)
            print("Pause Background When Animating", "=", '"' + str(self.check_box_pause.isChecked()) + '"', file=f)
            print("Use Video Background", "=", '"' + str(self.radio_btn_video_back.isChecked()) + '"', file=f)
            print("Use Image Background", "=", '"' + str(self.radio_btn_image_back.isChecked()) + '"', file=f)
            print("Background Video File Name", "=", '"' + str(self.line_back_video.displayText()) + '"', file=f)
            print("Background Image File Name", "=", '"' + str(self.line_back_image.displayText()) + '"', file=f)
            print("Logo Video File Name", "=", '"' + str(self.line_logo_video.displayText()) + '"', file=f)
            print("Margin Bottom", "=", '"' + str(self.spin_box_top.value()) + '"', file=f)
            print("Margin Top", "=", '"' + str(self.spin_box_bottom.value()) + '"', file=f)
            print("AnimationDuration", "=", '"' + str(self.line_duration.displayText()) + '"', file=f)
            print("RestoreLastSession", "=", '"' + str(self.check_last_session.isChecked()) + '"', file=f)
            print("Language", "=", '"' + str(self.comboBox_language.currentText()) + '"', file=f)

        f.close()

    def pref_cancel(self):
        self.close()


class Add_Team(QtWidgets.QDialog, Ui_Add_Item):
    def __init__(self):
        super(Add_Team, self).__init__()

        self.setupUi(self)

    def add_brow_img(self):  # выбор файла для Video Background
        # self.line_image.setText("")
        try:
            path_image = QFileDialog.getOpenFileNames(self,
                                                      caption="Open Image Team",
                                                      directory="res",
                                                      filter="*.jpg *.png")[0][0]
            self.line_image.setText(path_image)
        except IndexError:
            pass

    def add_ok(self):
        self.close()

    def add_cancel(self):
        self.close()
