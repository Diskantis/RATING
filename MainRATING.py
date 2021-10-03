# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
# from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTranslator

from UI_RATING import Ui_MainWindow, Ui_About
from dll import read_reference, create_player, VideoPlayer, Preference


class MainRATING(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainRATING, self).__init__(parent)

        self.pref = Preference()  # class dll.Preference

        self.setupUi(self)  # class UI_RATING.Ui_MainWindow

        self.load_def_ref()
        print("GIT")

        self.id = 1
        self.image = ""

        self.action_New.triggered.connect(self.create_new)  # button "New" menu "File"
        self.action_Open.triggered.connect(self.open_file)  # button "Open" menu "File"
        self.action_Save.triggered.connect(self.save_file)  # button "Save" menu "File"
        self.action_Exit.triggered.connect(self.exit)  # button "Exit" menu "File"
        self.action_Preferences.triggered.connect(self.preferences)  # button "Preferences" menu "Options"
        self.action_About.triggered.connect(self.about)  # button "About" menu "Help"

        self.btn_Add_Item.clicked.connect(self.add_item)  # button "Add Item"
        self.btn_Remove_Item.clicked.connect(self.remove_item)  # button "Add Item"
        self.btn_Swap_Items.clicked.connect(self.swap_item)  # button "Add Item"
        self.btn_Move_to_Pos.clicked.connect(self.move_item)  # button "Add Item"
        self.btn_Logo_Scene.clicked.connect(self.logo_scene)  # button "Logo/Scene"

    def load_def_ref(self):
        val = read_reference("reference.reg")  # func dll.load_def_ref
        chb_ply, chb_pus, rbt_vbg, rbt_ibg, lin_vbg, lin_ibg, lin_vlg, mar_top, mar_bot, ani_dur, chb_lse, cmb_lng = val

        self.pref.check_box_player.setChecked(chb_ply)
        self.pref.check_box_pause.setChecked(chb_pus)
        self.pref.radio_btn_video_back.setChecked(rbt_vbg)
        self.pref.radio_btn_image_back.setChecked(rbt_ibg)
        self.pref.line_back_video.setText(lin_vbg)
        self.pref.line_back_image.setText(lin_ibg)
        self.pref.line_logo_video.setText(lin_vlg)
        self.pref.spin_box_top.setValue(mar_top)
        self.pref.spin_box_bottom.setValue(mar_bot)
        self.pref.line_duration.setText(str(ani_dur))
        self.pref.check_last_session.setChecked(chb_lse)
        self.pref.comboBox_language.setCurrentText(cmb_lng)

        self.image = lin_ibg

        self.start_player()

        return self.image

    def start_player(self):
        self.player_1, self.player_2 = create_player()

        self.player_1.video.setFixedSize(app.desktop().availableGeometry().size())
        self.player_2.video.setFixedSize(app.desktop().availableGeometry().size())
        self.player_1.video.show()
        self.player_2.video.show()

    def create_new(self):
        pass

    def open_file(self):
        pass
        # path_op_preset = QFileDialog.getOpenFileNames()

    def save_file(self):
        pass
        # path_sv_preset = QFileDialog.getSaveFileName()

    def exit(self):
        self.player_1.close()
        self.player_2.close()
        self.close()

    def preferences(self):

        self.pref.show()
        # TAB VIDEO
        self.pref.check_box_player.stateChanged.connect(self.pref.check_player_stat_chang)  # check box Player internal
        self.pref.check_box_pause.stateChanged.connect(self.pref.check_pause_stat_chang)  # check box Pause animation

        self.pref.btn_bg_brow_vid.clicked.connect(self.pref.bg_brow_vid)  # button "Browse..." Background Video file
        self.pref.btn_bg_brow_img.clicked.connect(self.pref.bg_brow_img)  # button "Browse..." Background Image file
        self.pref.btn_lg_brow_vid.clicked.connect(self.pref.lg_brow_vid)  # button "Browse..." Logo Video file

        self.pref.radio_btn_video_back.clicked.connect(self.pref.video_back)  # radio button "Video file:"
        self.pref.radio_btn_image_back.clicked.connect(self.pref.image_back)  # radio button "Image file:"
        # TAB SCENE
        # TAB COMMON
        self.pref.interface_lang()
        # OK
        self.pref.btn_ok.clicked.connect(lambda: self.pref.ok(self.player_1, self.player_2))  # button OK
        self.pref.btn_ok.setAutoDefault(True)

        self.pref.btn_cancel.clicked.connect(self.pref.cancel)  # button CANCEL

    def about(self):
        self.About = Ui_About()  # class UI_RATING.Ui_About
        self.About.setupUi()

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def swap_item(self):
        pass

    def move_item(self):
        pass

    def logo_scene(self):
        self.player_1.video.setFullScreen(True)
        self.player_2.video.setFullScreen(True)

        if self.id == 1:
            self.player_2.video.hide()
            self.player_1.video.show()
            self.id -= 1
        elif self.id == 0:
            self.player_1.video.hide()
            self.player_2.video.show()
            self.id += 1

    def closeEvent(self, event):
        self.player_1.close()
        self.player_2.close()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    file_lng = read_reference("reference.reg")
    language = file_lng[11]

    translator = QTranslator()
    translator.load("./lang/" + language)
    if not app.installTranslator(translator):
        print("Can not install translation!")

    windows = MainRATING()
    windows.show()
    sys.exit(app.exec_())