import ast
import os
import re
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl, Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QLabel, QHBoxLayout

from UI_RATING import Ui_Preference


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


def create_player(name_1, path_1, name_2, path_2):
    player_1 = VideoPlayer(name_1, path_1)  # class dll.VideoPlayer
    player_2 = VideoPlayer(name_2, path_2)  # class dll.VideoPlayer
    return player_1, player_2


class VideoPlayer:
    def __init__(self, name, path):
        path = path

        self.video = QVideoWidget()
        self.video.setWindowTitle(name)
        # self.video.setFullScreen(True)
        # self.video.setFixedSize(app.desktop().availableGeometry().size())
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.video.move(1920, 0)
        # self.video.resize(1920, 1080)
        self.video.hide()

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def reload(self, path):
        self.playlist.clear()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def close(self):
        self.video.close()


class ImagePlayer:
    def __init__(self, path):
        path = path

        self.video = QVideoWidget()
        # self.video.setFullScreen(True)
        # self.video.setFixedSize(app.desktop().availableGeometry().size())
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.video.move(1920, 0)
        # self.video.resize(1920, 1080)
        self.video.hide()

        pixmap1 = QPixmap(path)
        pixmap1 = pixmap1.scaledToWidth(self.video.width())

        self.image = QLabel()
        self.image.setPixmap(pixmap1)

        layout_box = QHBoxLayout(self.video)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.image)

        pixmap2 = QPixmap("res/PLASHKA_БОРОДА.png")
        pixmap2 = pixmap2.scaledToWidth(200)
        self.image2 = QLabel(self.video)
        self.image2.setPixmap(pixmap2)
        self.image2.setFixedSize(pixmap2.size())

        p = self.video.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        self.image2.move(p)


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

    def video_back(self):
        pass

    def image_back(self):
        pass

    def radio_btn_grp(self):
        pass
        # self.grp_radio = QtWidgets.QButtonGroup()
        # self.grp_radio.setExclusive(True)
        #
        # self.grp_radio.addButton(self.radio_btn_video_back)
        # self.grp_radio.addButton(self.radio_btn_image_back)
        #
        # self.radio_btn_video_back.clicked.connect(self.video_back)
        # self.radio_btn_image_back.clicked.connect(self.image_back)
        #
        # self.groupVAlignment.buttonClicked['int'].connect(self.groupHAlignmentClicked)
        # self.grp_radio.buttonClicked.connect(self.pr)
        #
        # if self.Preference.radio_btn_video_back.setChecked(True) is True:
        #     self.player_1 = VideoPlayer(self.path_1)
        #
        # elif self.Preference.radio_btn_image_back.setChecked(True) is True:
        #     self.player_1 = VideoPlayer(self.image)

    def bg_brow_vid(self):  # выбор файла для Video Background
        path_vid_1 = QFileDialog.getOpenFileNames(caption="Open Video Background", directory="res")
        try:
            self.line_back_video.setText(path_vid_1[0][0])
            self.path_vid_1 = path_vid_1[0][0]
        except IndexError:
            pass

    def bg_brow_img(self):  # выбор файла для Image Background
        path_img = QFileDialog.getOpenFileNames(caption="Open Image Background", directory="res")
        try:
            self.line_back_image.setText(path_img[0][0])
            self.image = path_img[0][0]
        except IndexError:
            pass

    def lg_brow_vid(self):  # выбор файла для Video Logo
        path_vid_2 = QFileDialog.getOpenFileNames(caption="Open Video Logo", directory="res")
        try:
            self.line_logo_video.setText(path_vid_2[0][0])
            self.path_vid_2 = path_vid_2[0][0]
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

    def ok(self, pl_1, pl_2):
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

        pl_1.reload(self.line_back_video.displayText())
        pl_1.play()
        pl_2.reload(self.line_logo_video.displayText())
        pl_2.play()

        self.close()

    def cancel(self):
        self.close()
