# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTranslator

from UI_RATING import Ui_MainWindow, Ui_About
from DLL_RATING import clear_layout, team_widgets, team_widgets_rat, read_reference, start_player, \
    ImagePlayer, Preference, Add_Team, Widget_Team_Button, Widget_Team_Rating


class MainRATING(QMainWindow, Ui_MainWindow, ):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)  # class UI_RATING.Ui_MainWindow

        self.teams_properties = [0]  # список с параметрами команд кол. команд + (путь к файлу банера и имя команды)
        self.team_widgets_btn = []  # список виджетов команд с кнопками
        self.team_widgets_rat = []  # список виджетов команд с банерами
        self.select_team = {}
        self.logo_or_scene = 0

        self.on_last_session = self.load_def_ref()

        self.image_rating = ImagePlayer("Team Ranking")  # class dll.ImagePlayer

        if self.on_last_session:
            self.open_file("saves/autosave.sav")

        self.action_New.triggered.connect(self.create_new)  # button "New" menu"File"
        self.action_Open.triggered.connect(lambda: self.open_file())  # button "Open" menu "File"
        self.action_Save.triggered.connect(lambda: self.save_file(self.teams_properties))  # button "Save" menu "File"
        self.action_Exit.triggered.connect(self.exit)  # button "Exit" menu "File"
        self.action_Preferences.triggered.connect(self.preferences)  # button "Preferences" menu "Options"
        self.action_About.triggered.connect(self.about)  # button "About" menu "Help"

        self.btn_Add_Team.clicked.connect(self.add_new_team)  # button "Add Item"
        self.btn_Remove_Team.clicked.connect(self.remove_team)  # button "Add Item"
        self.btn_Swap_Teams.clicked.connect(self.swap_teams)  # button "Add Item"
        self.btn_Move_to_Pos.clicked.connect(self.move_team)  # button "Add Item"
        self.btn_Logo_Rating.clicked.connect(self.logo_rating)  # button "Logo/Rating"

    def click_team_widget(self):
        if self.team_widgets_btn is not None:
            for i in self.team_widgets_btn:
                self.my_widget = i
                self.my_widget.btn_Team.clicked.connect(self.click_team_widget_btn)
                self.my_widget.btn_Team.customContextMenuRequested.connect(self.my_widget.show_context_menu)
                # self.my_widget.edt_team.triggered.connect(self.menuWidget)
                # self.my_widget.itm_scale.triggered.connect(self.menuWidget)
                # self.my_widget.pos_scale.triggered.connect(self.menuWidget)
                # self.my_widget.pos_offset.triggered.connect(self.menuWidget)
                # self.my_widget.rem_team.triggered.connect(self.menuWidget)

    # def menuWidget(self):
    #     print(self.select_team)
    #     sender = self.sender()
    #     if sender.text() == "Edit":
    #         print("Edit")
    #     elif sender.text() == "Set item scale":
    #         print("Set item scale")
    #     elif sender.text() == "Set position scale":
    #         print("Set position scale")
    #     elif sender.text() == "Set position offset":
    #         print("Set position offset")
    #     elif sender.text() == "Remove":
    #         print("Remove")

    def click_team_widget_btn(self):
        sender = self.sender()
        if sender.isChecked() is False:
            self.select_team.pop(int(sender.text()), None)
        else:
            self.select_team.update({int(sender.text()): sender.isChecked()})

        def has_low_price(price):
            return self.select_team[price] is True

        check_true = list(filter(has_low_price, self.select_team.keys()))
        print(check_true)
        if len(check_true) == 2:
            self.btn_Remove_Team.setEnabled(True)
            self.btn_Move_to_Pos.setEnabled(False)
            self.btn_Swap_Teams.setEnabled(True)
        elif len(check_true) == 1:
            self.btn_Remove_Team.setEnabled(True)
            self.btn_Move_to_Pos.setEnabled(True)
            self.btn_Swap_Teams.setEnabled(False)
        elif len(check_true) > 2:
            self.btn_Remove_Team.setEnabled(True)
            self.btn_Move_to_Pos.setEnabled(False)
            self.btn_Swap_Teams.setEnabled(False)
        else:
            self.btn_Remove_Team.setEnabled(False)
            self.btn_Move_to_Pos.setEnabled(False)
            self.btn_Swap_Teams.setEnabled(False)

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
            if self.player_1 or self.player_2:
                pass
        except AttributeError:
            if os.path.isfile(lin_vbg or lin_ibg or lin_vlg):
                self.player_1, self.player_2 = start_player()  # func dll.start_player
            else:
                self.pref.line_back_video.clear()
                self.pref.line_back_image.clear()
                self.pref.line_logo_video.clear()

        return self.pref.check_last_session.isChecked()

    def create_new(self):

        clear_layout(self.v_Layout_frame_items)
        clear_layout(self.image_rating.v_Layout_grb_items_rat)

        self.teams_properties = [0]
        self.team_widgets_btn = []
        self.team_widgets_rat = []
        self.select_team.clear()

        self.btn_Remove_Team.setEnabled(False)
        self.btn_Move_to_Pos.setEnabled(False)
        self.btn_Swap_Teams.setEnabled(False)

    def open_file(self, path_op_preset=None):
        self.create_new()
        try:
            if path_op_preset is None:
                path_op_preset = QFileDialog.getOpenFileNames(self, caption="Open Teams Rating", directory="saves",
                                                              filter="*.sav")[0][0]
            else:
                path_op_preset = path_op_preset

            list_str = []
            with open(path_op_preset, "r") as f:
                for line in f.readlines():
                    line = line.strip("\n")
                    list_str.append(line)

            list_str[0] = int(list_str[0])
            self.teams_properties = list_str

            self.team_widgets_btn = team_widgets(list_str, self.v_Layout_frame_items)
            self.team_widgets_rat = team_widgets_rat(list_str, self.image_rating.v_Layout_grb_items_rat)

        except (IndexError, FileNotFoundError):
            pass

        # print(self.teams_properties)
        # print(self.team_widgets_btn)
        # print(self.team_widgets_rat)
        # print(self.select_team)
        # print(self.v_Layout_frame_items.count())
        # print(self.image_rating.v_Layout_grb_items_rat.count())

        self.click_team_widget()

    def save_file(self, teams_properties, path_sv_preset=None):
        if path_sv_preset is None:
            path_sv_preset = QFileDialog.getSaveFileName(self, caption="Save Teams Rating", directory="saves",
                                                         filter="*.sav")[0]
        else:
            path_sv_preset = path_sv_preset
        teams_properties[0] = str(teams_properties[0])
        try:
            with open(path_sv_preset, "w") as f:
                for line in teams_properties:
                    f.write(f'{line}\n')
        except (IndexError, FileNotFoundError):
            pass

    def exit(self):
        self.save_file(self.teams_properties, path_sv_preset="saves/autosave.sav")
        try:
            if self.player_1 and self.player_2:
                self.player_1.close()
                self.player_2.close()
                self.image_rating.close()
                self.close()
        except AttributeError:
            self.image_rating.close()
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
        self.pref.interface_lang()  # comboBox с выбором языка программы

        # OK
        self.pref.btn_ok.clicked.connect(self.preferences_ok)  # button OK
        self.pref.btn_ok.setAutoDefault(True)

        self.pref.btn_cancel.clicked.connect(self.pref.pref_cancel)  # button CANCEL

    def preferences_ok(self):
        try:
            if self.player_1 and self.player_2:  # если плеера запущены
                self.pref.save_preferences()  # сохраняем параметры

                self.player_1.video.close()  # закрываем плеер
                self.player_2.video.close()  # закрываем плеер

                self.player_1, self.player_2 = start_player()  # запускаем плеера с новыми параметрами

                val = read_reference("reference.reg")  # считываем параметры margins (top, bottom)
                self.image_rating.v_Layout_grb_items_rat.setContentsMargins(0, val[7], 0, val[8])
                self.image_rating.video.activateWindow()  # делает окно рейтинга активным

            if self.logo_or_scene == 1:  # если кнопка Logo/Rating была в положение Logo меняет на Rating
                self.logo_or_scene -= 1
                self.btn_Logo_Rating.setChecked(False)
                self.btn_Logo_Rating.setText("R A T I N G")

            self.pref.close()

        except AttributeError:
            self.pref.save_preferences()  # сохраняем параметры
            self.player_1, self.player_2 = start_player()  # если плеера не были запущены - запускает плеера
            self.pref.close()

    def about(self):
        self.About = Ui_About()  # class UI_RATING.Ui_About
        self.About.setupUi()
        self.About.show()

    def add_new_team(self):
        self.add_team = Add_Team()
        self.add_team.show()

        self.add_team.btn_brow_image.clicked.connect(self.add_team.add_team_brow_img)  # button "Browse..." Item Image

        self.add_team.btn_ok.clicked.connect(self.add_new_team_ok)  # button OK
        self.add_team.btn_ok.setAutoDefault(True)

        self.add_team.btn_cancel.clicked.connect(self.add_team.add_cancel)  # button

    def add_new_team_ok(self):
        if self.add_team.line_image.displayText() and self.add_team.line_text.displayText():

            prop = [self.add_team.line_image.displayText(), self.add_team.line_text.displayText()]
            index = str(self.v_Layout_frame_items.count() + 1)

            self.team = Widget_Team_Button(index, self.add_team.line_text.displayText())
            self.v_Layout_frame_items.addWidget(self.team)

            self.team_rat = Widget_Team_Rating(self.add_team.line_image.displayText())
            self.image_rating.v_Layout_grb_items_rat.addWidget(self.team_rat)

            self.add_team.close()

            self.teams_properties[0] += 1
            self.teams_properties += prop

            self.team_widgets_btn.append(self.team)
            self.team_widgets_rat.append(self.team_rat)

            self.click_team_widget()

    def remove_team(self):
        pos = list(self.select_team.keys())
        pos.sort(reverse=True)
        for i in pos:
            self.team_widgets_btn.pop(i - 1)
            self.teams_properties.pop(i * 2)
            self.teams_properties.pop(i * 2 - 1)
            self.teams_properties[0] -= 1

            team_btn = self.v_Layout_frame_items.itemAt(i - 1).widget()  # удаляет виджет с кнопкой
            self.v_Layout_frame_items.removeWidget(team_btn)

            team_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(i - 1).widget()  # удаляет виджет с банером
            self.image_rating.v_Layout_grb_items_rat.removeWidget(team_rat)

        clear_layout(self.v_Layout_frame_items)
        clear_layout(self.image_rating.v_Layout_grb_items_rat)

        self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
        self.team_widgets_rat = team_widgets_rat(self.teams_properties, self.image_rating.v_Layout_grb_items_rat)

        self.select_team.clear()

        self.btn_Remove_Team.setEnabled(False)
        self.btn_Swap_Teams.setEnabled(False)
        self.btn_Move_to_Pos.setEnabled(False)

        self.click_team_widget()

        print(self.teams_properties)
        print(self.team_widgets_btn)
        print(self.team_widgets_rat)
        print(self.select_team)
        print(self.v_Layout_frame_items.count())
        print(self.image_rating.v_Layout_grb_items_rat.count())

    def swap_teams(self):
        pos = list(self.select_team.keys())
        pos.sort(reverse=True)
        index_1, index_2 = pos  # инедксы виджетов выбраных для перемещения

        team_1 = self.v_Layout_frame_items.itemAt(index_1 - 1).widget()  # виджет выбраный для перемещения
        team_2 = self.v_Layout_frame_items.itemAt(index_2 - 1).widget()  # виджет выбраный для перемещения

        team_replace = self.v_Layout_frame_items.replaceWidget(team_2, team_1)  # Item с виджетом team_2
        self.v_Layout_frame_items.insertWidget(index_1 - 1, team_replace.widget())  # вставляем виджет team_2

        team_1_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(index_1-1).widget()
        team_2_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(index_2-1).widget()

        team_replace_rat = self.image_rating.v_Layout_grb_items_rat.replaceWidget(team_2_rat, team_1_rat)
        self.image_rating.v_Layout_grb_items_rat.insertWidget(index_1-1, team_replace_rat.widget())

        team_w = self.team_widgets_btn.pop(index_1 - 1)
        self.team_widgets_btn.insert(index_2 - 1, team_w)
        team_w_rat = self.team_widgets_rat.pop(index_1 - 1)
        self.team_widgets_rat.insert(index_2 - 1, team_w_rat)

        team_p1_1 = self.teams_properties.pop(index_1 * 2)
        team_p1_2 = self.teams_properties.pop(index_1 * 2 - 1)
        team_p2_1 = self.teams_properties.pop(index_2 * 2)
        team_p2_2 = self.teams_properties.pop(index_2 * 2 - 1)

        self.teams_properties.insert(index_2 * 2 - 1, team_p1_1)
        self.teams_properties.insert(index_2 * 2 - 1, team_p1_2)
        self.teams_properties.insert(index_1 * 2 - 1, team_p2_1)
        self.teams_properties.insert(index_1 * 2 - 1, team_p2_2)

        clear_layout(self.v_Layout_frame_items)
        clear_layout(self.image_rating.v_Layout_grb_items_rat)
        self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
        self.team_widgets_rat = team_widgets_rat(self.teams_properties, self.image_rating.v_Layout_grb_items_rat)

        team_1 = self.v_Layout_frame_items.itemAt(index_1 - 1).widget()
        team_2 = self.v_Layout_frame_items.itemAt(index_2 - 1).widget()
        team_1.btn_Team.setChecked(True)
        team_2.btn_Team.setChecked(True)

        self.lineEdit_Pos.setText("")

        self.click_team_widget()

    def move_team(self):
        index = (list(self.select_team.keys())[0])-1  # инедкс виджета выбраного для перемещения
        try:
            position = (int(self.lineEdit_Pos.displayText()))-1  # номер позиции куда перемещаем виджет

            if 0 <= position <= self.v_Layout_frame_items.count():
                if position <= 1:
                    team_1 = self.v_Layout_frame_items.itemAt(index).widget()
                    team_2 = self.v_Layout_frame_items.itemAt(position).widget()
                    team_replace = self.v_Layout_frame_items.replaceWidget(team_2, team_1)
                    self.v_Layout_frame_items.insertWidget(position + 1, team_replace.widget())

                    team_1 = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()
                    team_2 = self.image_rating.v_Layout_grb_items_rat.itemAt(position).widget()
                    team_replace = self.image_rating.v_Layout_grb_items_rat.replaceWidget(team_2, team_1)
                    self.image_rating.v_Layout_grb_items_rat.insertWidget(position + 1, team_replace.widget())

                elif position < self.v_Layout_frame_items.count():
                    team_1 = self.v_Layout_frame_items.itemAt(index).widget()
                    team_2 = self.v_Layout_frame_items.itemAt(position-1).widget()
                    team_replace = self.v_Layout_frame_items.replaceWidget(team_2, team_1)
                    self.v_Layout_frame_items.insertWidget(position-1, team_replace.widget())

                    team_1 = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()
                    team_2 = self.image_rating.v_Layout_grb_items_rat.itemAt(position-1).widget()
                    team_replace = self.image_rating.v_Layout_grb_items_rat.replaceWidget(team_2, team_1)
                    self.image_rating.v_Layout_grb_items_rat.insertWidget(position-1, team_replace.widget())

                team_w = self.team_widgets_btn.pop(index)
                self.team_widgets_btn.insert(position, team_w)

                team_p1 = self.teams_properties.pop(index * 2 + 2)
                team_p2 = self.teams_properties.pop(index * 2 + 1)
                self.teams_properties.insert(position * 2 + 1, team_p1)
                self.teams_properties.insert(position * 2 + 1, team_p2)

                clear_layout(self.v_Layout_frame_items)
                clear_layout(self.image_rating.v_Layout_grb_items_rat)

                self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
                self.team_widgets_rat = team_widgets_rat(self.teams_properties,
                                                         self.image_rating.v_Layout_grb_items_rat)

                self.select_team.clear()

                team_2 = self.v_Layout_frame_items.itemAt(position).widget()
                team_2.btn_Team.setChecked(True)
                self.select_team[position+1] = True

                self.lineEdit_Pos.setText("")

                self.click_team_widget()

        except ValueError:
            pass

    def logo_rating(self):
        try:
            if self.player_1 and self.player_2:
                if self.logo_or_scene == 0:
                    self.player_2.video.activateWindow()
                    self.logo_or_scene += 1
                    self.btn_Logo_Rating.setText("L O G O")
                elif self.logo_or_scene == 1:
                    self.player_1.video.activateWindow()
                    self.image_rating.video.activateWindow()
                    self.logo_or_scene -= 1
                    self.btn_Logo_Rating.setText("R A T I N G")
        except AttributeError:
            pass

    # def mousePressEvent(self, event):
        #     button = event.button()
        #     if button == Qt.Qt.RightButton:
        #         print("Right button click!")
        #     elif button == Qt.Qt.LeftButton:
        #         print("Left button click!")
        #
        # def mouseReleaseEvent(self, event):
        #     pass

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
