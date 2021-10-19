import ast
import os
import re

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QLabel, QHBoxLayout, QWidget

from UI_RATING import Ui_Preference, Ui_Add_Team, Ui_Widget_Team


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
    for i in list_str[2:len(list_str) + 1:2]:
        index = str(layout.count() + 1)
        team = Widget_Team(index, i)
        layout.addWidget(team)
        widgets.append(team)  # создаем список с виджетами команд
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
        except:
            return value

    list_data = [real_type(i) for i in list_str]
    return list_data


def start_player():
    val = read_reference("reference.reg")
    if val[2]:
        player_1 = VideoPlayer("Video Background", val[4])  # class dll.VideoPlayer
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        return player_1, player_2  #, image_rating
    elif val[3]:
        player_1 = ImagePlayer("Image Background", val[5])  # class dll.ImagePlayer
        player_2 = VideoPlayer("Video Logo", val[6])  # class dll.VideoPlayer
        return player_1, player_2


class VideoPlayer:
    def __init__(self, name, path=None):
        self.video = QVideoWidget()
        self.video.setWindowTitle(name)
        self.video.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        # self.video.move(1920, 0)
        # self.video.setFixedSize(1920, 1080)
        # self.video.setFullScreen(True)
        self.video.move(10, 10)
        self.video.setFixedSize(800, 600)

        if path is not None:
            self.playlist = QMediaPlaylist()
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

            self.player = QMediaPlayer()
            self.player.setVideoOutput(self.video)
            self.player.setPlaylist(self.playlist)
            self.player.play()

        self.video.show()

    def close(self):
        self.video.close()


class ImagePlayer:
    def __init__(self, name, path=None):
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

        if path is not None:
            pixmap1 = QPixmap(path)
            pixmap1 = pixmap1.scaledToWidth(self.video.width())
            self.image1.setPixmap(pixmap1)

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
    def margins(self):
        pass

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
            f.write(f'Margin Bottom = "{str(self.spin_box_top.value())}"\n')
            f.write(f'Margin Top = "{str(self.spin_box_bottom.value())}"\n')
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


class Widget_Team(QtWidgets.QWidget, Ui_Widget_Team):
    clicked = pyqtSignal()

    def __init__(self, index, name):
        super(Widget_Team, self).__init__()

        self.setupUi(self)

        # # кнопка с названием команды
        self.btn_Team.setText(index)
        self.label_name_team.setText(name)
        self.btn_Team.customContextMenuRequested.connect(self.show_context_menu)

        self.edt_team.triggered.connect(self.edit_team)
        self.itm_scale.triggered.connect(self.item_scale)
        self.pos_scale.triggered.connect(self.position_scale)
        self.pos_offset.triggered.connect(self.position_offset)
        self.rem_team.triggered.connect(self.remove_team)

    def show_context_menu(self, point):
        self.menuTeam.exec(self.btn_Team.mapToGlobal(point))

    def edit_team(self):
        self.edit_team = Add_Team()
        self.edit_team.setWindowTitle("Edit team")
        self.edit_team.show()

        self.edit_team.btn_cancel.clicked.connect(self.edit_team.add_cancel)  # button CANCEL

        # def add_check(self):
        #     try:
        #         if self.team:
        #             self.add_team.close()
        #     except AttributeError:
        #         self.add_team.add_team_save()
        #         self.team = Widget_Team(self.add_team.line_text.displayText())
        #         self.v_Layout_frame_items.addWidget(self.team)
        #         self.add_team.close()

    def item_scale(self):
        pass

    def position_scale(self):
        pass

    def position_offset(self):
        pass

    def remove_team(self):
        pass
