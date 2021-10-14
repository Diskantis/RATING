# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTranslator

from UI_RATING import Ui_MainWindow, Ui_About
from DLL_RATING import read_reference, start_player, Preference, Add_Team, Widget_Team


class MainRATING(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)  # class UI_RATING.Ui_MainWindow

        self.teams_properties = [0]

        self.load_def_ref()

        self.id = 1
        self.v_Layout_frame_items.count()

        self.action_New.triggered.connect(self.create_new)  # button "New" menu "File"
        self.action_Open.triggered.connect(self.open_file)  # button "Open" menu "File"
        self.action_Save.triggered.connect(lambda: self.save_file(self.teams_properties))  # button "Save" menu "File"
        self.action_Exit.triggered.connect(self.exit)  # button "Exit" menu "File"
        self.action_Preferences.triggered.connect(self.preferences)  # button "Preferences" menu "Options"
        self.action_About.triggered.connect(self.about)  # button "About" menu "Help"

        self.btn_Add_Team.clicked.connect(self.add_new_team)  # button "Add Item"
        self.btn_Remove_Team.clicked.connect(self.remove_team)  # button "Add Item"
        self.btn_Swap_Teams.clicked.connect(self.swap_teams)  # button "Add Item"
        self.btn_Move_to_Pos.clicked.connect(self.move_team)  # button "Add Item"
        self.btn_Logo_Scene.clicked.connect(self.logo_scene)  # button "Logo/Scene"

        # try:
        #     if self.teams_properties[0] > 0:
        #         self.myWidget = self.v_Layout_frame_items.itemAt(0).widget()
        #
        #         print(self.myWidget)
        # except:
        #     pass

    # def click(self):
    #     print("Checkedaaaaaa:", self.btn_Team.isChecked())

    def load_def_ref(self):
        self.pref = Preference()  # class dll.Preference
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

        try:
            if self.player_1 and self.player_2:
                pass
        except AttributeError:
            if os.path.isfile(lin_vbg or lin_ibg or lin_vlg):
                pass
                # self.player_1, self.player_2 = start_player()
            else:
                self.pref.line_back_video.clear()
                self.pref.line_back_image.clear()
                self.pref.line_logo_video.clear()

    def create_new(self):
        pass

    def open_file(self):
        path_op_preset = QFileDialog.getOpenFileNames(self, caption="Open Teams Rating", directory="saves",
                                                      filter="*.sav")[0][0]
        list_str = []
        with open(path_op_preset, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                list_str.append(line)

        for i in list_str[2:len(list_str) + 1:2]:
            index = str(self.v_Layout_frame_items.count() + 1)
            self.team = Widget_Team(index, i)
            self.v_Layout_frame_items.addWidget(self.team)

        list_str[0] = int(list_str[0])
        self.teams_properties = list_str

        # for a in list_str[1:len(list_str) + 1]:
        #     self.teams_properties[0] += 1
        #     self.teams_properties += a
        # print(self.teams_properties)

        # index = self.v_Layout_frame_items.count()
        # print(index)
        # myWidget = self.v_Layout_frame_items.itemAt(1).widget()
        # if myWidget.btn_Team.isChecked():
        #     print("dsfa")
        # print(myWidget.btn_Team.isChecked())
        # print(myWidget.btn_Team.text(), myWidget.label_name_team.text())

    def save_file(self, teams_properties):
        path_sv_preset = QFileDialog.getSaveFileName(self, caption="Save Teams Rating", directory="saves",
                                                     filter="*.sav")[0]
        teams_properties[0] = str(teams_properties[0])
        save_file = open(path_sv_preset, "w")
        for line in teams_properties:
            save_file.write(line)
            save_file.write('\n')
        save_file.close()

    def exit(self):
        try:
            if self.player_1 and self.player_2:
                self.player_1.close()
                self.player_2.close()
                self.close()
        except AttributeError:
            self.close()

    def preferences(self):
        self.load_def_ref()
        self.pref.show()

        # TAB VIDEO
        self.pref.check_box_player.stateChanged.connect(self.pref.check_player_stat_chang)  # check box Player internal
        self.pref.check_box_pause.stateChanged.connect(self.pref.check_pause_stat_chang)  # check box Pause animation

        self.pref.btn_bg_brow_vid.clicked.connect(self.pref.bg_brow_vid)  # button "Browse..." Background Video file
        self.pref.btn_bg_brow_img.clicked.connect(self.pref.bg_brow_img)  # button "Browse..." Background Image file
        self.pref.btn_lg_brow_vid.clicked.connect(self.pref.lg_brow_vid)  # button "Browse..." Logo Video file

        # TAB COMMON
        self.pref.interface_lang()

        # OK
        self.pref.btn_ok.clicked.connect(self.pref_check)  # button OK
        self.pref.btn_ok.setAutoDefault(True)

        self.pref.btn_cancel.clicked.connect(self.pref.pref_cancel)  # button CANCEL

    def pref_check(self):
        try:
            if self.player_1 and self.player_2:
                self.pref_ok(self.player_1, self.player_2)
        except AttributeError:
            self.pref.save_preferences()
            self.player_1, self.player_2 = start_player()  # func dll.start_player
            self.pref.close()

    def pref_ok(self, pl_1, pl_2):
        self.pref.save_preferences()

        pl_1.video.close()
        pl_2.video.close()

        self.player_1, self.player_2 = start_player()  # func dll.start_player

        self.pref.close()

    def about(self):
        self.About = Ui_About()  # class UI_RATING.Ui_About
        self.About.setupUi()
        self.About.show()

    def add_new_team(self):
        self.add_team = Add_Team()
        self.add_team.show()

        self.add_team.btn_brow_image.clicked.connect(self.add_team.add_team_brow_img)  # button "Browse..." Item Image

        self.add_team.btn_ok.clicked.connect(self.add_team_ok)  # button OK
        self.add_team.btn_ok.setAutoDefault(True)

        self.add_team.btn_cancel.clicked.connect(self.add_team.add_cancel)  # button

    def add_team_ok(self):
        prop = [self.add_team.line_image.displayText(), self.add_team.line_text.displayText()]
        index = str(self.v_Layout_frame_items.count() + 1)
        self.team = Widget_Team(index, self.add_team.line_text.displayText())
        self.v_Layout_frame_items.addWidget(self.team)

        self.add_team.close()

        self.teams_properties[0] += 1
        self.teams_properties += prop
        print(self.teams_properties)

    def remove_team(self):
        pass

    def swap_teams(self):
        pass

    def move_team(self):
        pass

    def logo_scene(self):
        try:
            if self.player_1 and self.player_2:
                if self.id == 1:
                    self.player_2.video.hide()
                    self.player_1.video.show()
                    self.id -= 1
                    self.btn_Logo_Scene.setText("S C E N E")
                elif self.id == 0:
                    self.player_1.video.hide()
                    self.player_2.video.show()
                    self.id += 1
                    self.btn_Logo_Scene.setText("L O G O")
        except AttributeError:
            pass

    def closeEvent(self, event):
        self.exit()


def application():
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


if __name__ == "__main__":
    application()
