# -*- coding: utf-8 -*-
import os
import re
import ast
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QLabel, QHBoxLayout
from PyQt5.QtCore import QUrl, QPoint, Qt
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QTranslator

from UI_REITING import Ui_MainWindow, Ui_Preference, About


class VideoPlayer:
    def __init__(self, path):
        path = path

        self.video = QVideoWidget()
        # self.video.setFullScreen(True)
        # self.video.setFixedSize(app.desktop().availableGeometry().size())
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.video.move(10, 10)
        self.video.resize(800, 600)
        self.video.hide()

        self.playlist(path)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        self.player.setPlaylist(self.playlist)
        self.player.play()

        # pixmap1 = QPixmap("res/002_Desktop Wallpapers  HD Part (162).jpg")
        # pixmap1 = pixmap1.scaledToWidth(self.video.width())
        #
        # self.image = QLabel()
        # self.image.setPixmap(pixmap1)
        #
        # layout_box = QHBoxLayout(self.video)
        # layout_box.setContentsMargins(0, 0, 0, 0)
        # layout_box.addWidget(self.image)
        #
        # pixmap2 = QPixmap("res/PLASHKA_БОРОДА.png")
        # pixmap2 = pixmap2.scaledToWidth(200)
        # self.image2 = QLabel(self.video)
        # self.image2.setPixmap(pixmap2)
        # self.image2.setFixedSize(pixmap2.size())
        #
        # p = self.video.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        # self.image2.move(p)

    def playlist(self, file):
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        return self.playlist

    def close(self):
        self.video.close()


class Preference(QtWidgets.QWidget, Ui_Preference):
    def __init__(self):
        super(Preference, self).__init__()

        self.setupUi(self)

        self.path_1, self.path_2, self.image = "", "", "",

        self.interface_lang()

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
        path_1 = QFileDialog.getOpenFileNames()
        try:
            self.line_back_video.setText(path_1[0][0])
            self.path_1 = path_1[0][0]
        except IndexError:
            pass
        return self.path_1

    def bg_brow_img(self):  # выбор файла для Image Background
        path_img = QFileDialog.getOpenFileNames()
        try:
            self.line_back_image.setText(path_img[0][0])
            self.image = path_img[0][0]
        except IndexError:
            pass
        return self.image

    def lg_brow_vid(self):  # выбор файла для Logo
        path_vid_2 = QFileDialog.getOpenFileNames()
        try:
            self.line_logo_video.setText(path_vid_2[0][0])
            self.path_2 = path_vid_2[0][0]
        except IndexError:
            pass
        return self.path_2

    # TAB SCENE
    # TAB COMMON

    def interface_lang(self):  # выбор языка интерфейса
        path = "../lang"
        language = filter(lambda x: x.lower().endswith(('.qm', )), os.listdir(path))
        self.comboBox_language.addItems(language)

    # OK

    def ok(self, pl_1, pl_2):
        with open("reference.txt", "w") as f:
            print("Use Internal Video Player", "=", '"' + str(self.check_box_player.isChecked()) + '"', file=f)
            print("Pause Background When Animating", "=", '"' + str(self.check_box_pause.isChecked()) + '"', file=f)
            print("Use Video Background", "=", '"' + str(self.radio_btn_video_back.isChecked()) + '"', file=f)
            print("Use Image Background", "=", '"' + str(self.radio_btn_image_back.isChecked()) + '"', file=f)
            print("Background Video File Name", "=", '"' + str(self.line_back_video.displayText()) + '"', file=f)
            print("Background Image File Name", "=", '"' + str(self.line_back_image.displayText()) + '"', file=f)
            print("Logo Video File Name", "=", '"' + str(self.line_logo_video.displayText()) + '"', file=f)
            # print("BottomMargin", "=", '"' + str() + '"', file=f)
            # print("TopMargin", "=", '"' + str() + '"', file=f)
            # print("AnimationDuration", "=", '"' + str() + '"', file=f)
            print("RestoreLastSession", "=", '"' + str(self.check_last_session.isChecked()) + '"', file=f)
            print("Language", "=", '"' + str(self.comboBox_language.currentText()) + '"', file=f)

            # ch_pl, ch_pu, rb_vb, rb_ib, li_vb, li_ib, li_vl, cb_lng, mar_top, mar_bot, ani_dur

        # self.path_1 = self.line_back_video.displayText()
        # self.path_2 = self.line_logo_video.displayText()
        # self.image = self.line_back_image.displayText()
        #
        # self.player_1 = VideoPlayer(self.path_1)
        # self.player_2 = VideoPlayer(self.path_2)

        pl_1.close()
        pl_2.close()

        print(pl_1)
        print(pl_2)

        self.close()

    def cancel(self):
        self.close()

    def __str__(self):
        return self.path_1, self.path_2, self.image


class MainREITING(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainREITING, self).__init__(parent)

        self.pref = Preference()
        self.About = About()

        self.setupUi(self)

        self.id = 1
        self.path_1, self.path_2, self.image = "", "", ""

        self.load_def_ref()

        self.player_1 = VideoPlayer(self.path_1)
        self.player_2 = VideoPlayer(self.path_2)

        self.action_New.triggered.connect(self.create_new)  # button "New" menu "File"
        self.action_Open.triggered.connect(self.open_file)  # button "Open" menu "File"
        self.action_Save.triggered.connect(self.save_file)  # button "Save" menu "File"
        self.action_Exit.triggered.connect(self.exit)  # button "Exit" menu "File"
        self.action_Preferences.triggered.connect(self.preferences)  # button "Preferences" menu "Options"
        self.action_About.triggered.connect(self.about)  # button "About" menu "Help"

        self.btn_Logo_Scene.clicked.connect(self.logo_scence)  # button "Logo/Scene"

        # print(self.player_1)
        # print(self.player_2)

    def load_def_ref(self):
        val = ""
        with open("reference.txt", "r") as f:
            for line in f.readlines():
                val += line.strip("\n")
        val = re.findall(r'"(.*?)"', val)

        def real_type(value):  # изменяет тип данных в зависимости от их типа (str -> bool, str -> int или float)
            try:
                return ast.literal_eval(value)
            except:
                return value

        val = [real_type(i) for i in val]
        chb_ply, chb_pus, rbt_vbg, rbt_ibg, lin_vbg, lin_ibg, lin_vlg, chb_lse, cmb_lng = val
        # chb_ply, chb_pus, rbt_vbg, rbt_ibg, lin_vbg, lin_ibg, lin_vlg, mar_top, mar_bot, ani_dur, chb_lse, cmb_lng

        self.pref.check_box_player.setChecked(chb_ply)
        self.pref.check_box_pause.setChecked(chb_pus)
        self.pref.radio_btn_video_back.setChecked(rbt_vbg)
        self.pref.radio_btn_image_back.setChecked(rbt_ibg)
        self.pref.line_back_video.setText(lin_vbg)
        self.pref.line_back_image.setText(lin_ibg)
        self.pref.line_logo_video.setText(lin_vlg)

        self.pref.check_last_session.setChecked(chb_lse)
        self.pref.comboBox_language.setCurrentText(cmb_lng)

        self.path_1, self.path_2, self.image = lin_vbg, lin_vlg, lin_ibg

        return self.path_1, self.path_2, self.image

    def create_new(self):
        pass

    def open_file(self):
        path_op_preset = QFileDialog.getOpenFileNames()

    def save_file(self):
        path_sv_preset = QFileDialog.getSaveFileName()

    def exit(self):
        self.player_1.close()
        self.player_2.close()
        self.close()

    def preferences(self):
        self.pref.show()

        # check box Player internal
        self.pref.check_box_player.stateChanged.connect(self.pref.check_player_stat_chang)
        # check box Pause animation
        self.pref.check_box_pause.stateChanged.connect(self.pref.check_pause_stat_chang)

        self.pref.btn_bg_brow_vid.clicked.connect(self.pref.bg_brow_vid)  # button "Browse..." Background Video file
        self.pref.btn_bg_brow_img.clicked.connect(self.pref.bg_brow_img)  # button "Browse..." Background Image file
        self.pref.btn_lg_brow_vid.clicked.connect(self.pref.lg_brow_vid)  # button "Browse..." Logo Video file

        self.pref.radio_btn_video_back.clicked.connect(self.pref.video_back)  # radio button "Video file:"
        self.pref.radio_btn_image_back.clicked.connect(self.pref.image_back)  # radio button "Image file:"

        self.pref.btn_ok.clicked.connect(lambda: self.pref.ok(self.player_1, self.player_2))  # button OK
        # self.pref.btn_ok.clicked.connect(self.pref.ok)  # button OK
        self.pref.btn_ok.setAutoDefault(True)

        self.pref.btn_cancel.clicked.connect(self.pref.cancel)  # button CANCEL

    def about(self):
        self.About.setupUi()

    def logo_scence(self):
    # if self.player_1 or self.player_2:
        if self.id == 1:
            self.player_2.video.hide()
            self.player_1.video.show()
            self.id -= 1
        elif self.id == 0:
            self.player_1.video.hide()
            self.player_2.video.show()
            self.id += 1
    # else:
    #     self.load_def_ref()
    #     self.player_1 = VideoPlayer(self.path_1)
    #     self.player_2 = VideoPlayer(self.path_2)

    def closeEvent(self, event):
        self.player_1.close()
        self.player_2.close()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    translator = QTranslator()
    # translator.load("./lang/REITIG_UI_1_ru.qm")
    # if not app.installTranslator(translator):
    #     print("Can not install translation!")

    windows = MainREITING()
    windows.show()
    sys.exit(app.exec_())
