# -*- coding: utf-8 -*-
import ast
import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTranslator, QPoint, QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QTimer, QSize

from UI_RATING import Ui_MainWindow, Ui_About
from DLL_RATING import update_layout, clear_layout, team_widgets, team_widgets_rat, read_reference, \
    start_player, ImagePlayer, Preference, Add_Team, Menu_Team, Widget_Team_Button, Widget_Team_Rating, Position_Offset


class MainRATING(QMainWindow, Ui_MainWindow, ):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)  # class UI_RATING.Ui_MainWindow

        self.teams_properties = []  # список с параметрами команд кол. команд + (путь к файлу банера и имя команды)
        self.team_widgets_btn = []  # список виджетов команд с кнопками
        self.team_widgets_rat = []  # список виджетов команд с банерами
        self.select_team = {}  # словарь выделенных виджетов
        self.index_btn = None  # индекс кнопки при вызове меню (правая кнопка мыши)
        self.contents_margin = 0, 0, 0, 0  # отступы главного окна
        self.animation_duration = 1000  # длительность анимации
        self.logo_or_rating = 0

        self.on_last_session, self.on_animation_pause, self.contents_margin, self.animation_duration = \
            self.load_def_ref()

        self.image_rating = ImagePlayer("Team Ranking")  # создаем окно с рейтингом команд

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
            for self.my_widget in self.team_widgets_btn:
                self.my_widget.btn_Team.clicked.connect(self.left_click_team_widget_btn)
                self.my_widget.btn_Team.customContextMenuRequested.connect(self.right_click_team_widget_btn)
                self.my_widget.edt_team.triggered.connect(self.right_click_edit_team)
                self.my_widget.itm_scale.triggered.connect(self.right_click_item_scale)
                self.my_widget.pos_scale.triggered.connect(self.right_click_position_scale)
                self.my_widget.pos_offset.triggered.connect(self.right_click_position_offset)
                self.my_widget.rem_team.triggered.connect(self.right_click_remove_team)

    def left_click_team_widget_btn(self):
        sender = self.sender()
        if sender.isChecked() is False:
            self.select_team.pop(int(sender.text()), None)
        else:
            self.select_team.update({int(sender.text()): sender.isChecked()})

        def has_low_price(price):
            return self.select_team[price] is True

        check_true = list(filter(has_low_price, self.select_team.keys()))

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

    def right_click_team_widget_btn(self, point):
        sender = self.sender()
        self.index_btn = int(sender.text())

        self.team = self.v_Layout_frame_items.itemAt(self.index_btn - 1).widget()
        self.team.menuTeam.exec(self.team.btn_Team.mapToGlobal(point))

    def right_click_edit_team(self):
        index = self.index_btn - 1

        team_path_img, team_name = self.teams_properties[index][0], self.teams_properties[index][1]

        self.edit_team = Add_Team()
        _translate = QtCore.QCoreApplication.translate
        self.edit_team.setWindowTitle(_translate("MainWindow", "Edit team"))
        self.edit_team.line_image.setText(team_path_img)
        self.edit_team.line_text.setText(team_name)
        self.edit_team.show()

        self.edit_team.btn_brow_image.clicked.connect(self.edit_team.add_team_brow_img)  # Item Image "Browse..."

        self.edit_team.btn_ok.clicked.connect(self.right_click_edit_team_ok)  # button OK
        self.edit_team.btn_ok.setAutoDefault(True)

        self.edit_team.btn_cancel.clicked.connect(self.edit_team.add_cancel)  # button CANCEL

    def right_click_edit_team_ok(self):
        index = self.index_btn - 1

        self.teams_properties[index][0] = self.edit_team.line_image.displayText()
        self.teams_properties[index][1] = self.edit_team.line_text.displayText()

        clear_layout(self.v_Layout_frame_items)
        clear_layout(self.image_rating.v_Layout_grb_items_rat)

        self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
        self.team_widgets_rat = team_widgets_rat(self.teams_properties, self.image_rating.v_Layout_grb_items_rat)

        update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)
        self.edit_team.close()
        self.click_team_widget()

    def right_click_item_scale(self):
        self.item_scale = Menu_Team()
        self.item_scale.show()

        index = self.index_btn - 1
        item_scale = self.teams_properties[index][3]
        self.item_scale.line_parameter.setText(str(item_scale))

        self.item_scale.btn_ok.clicked.connect(self.right_click_item_scale_ok)  # button OK
        self.item_scale.btn_ok.setAutoDefault(True)

        self.item_scale.btn_cancel.clicked.connect(self.item_scale.menu_cancel)  # button

    def right_click_item_scale_ok(self):
        index = self.index_btn - 1
        pos_scale = float(self.item_scale.line_parameter.displayText())
        self.team = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()

        self.teams_properties[index][3] = pos_scale

        width = self.team.pixmap.width()
        self.pixmap = self.team.pixmap.scaledToWidth(int(width * pos_scale))
        self.team.image_team.setPixmap(self.pixmap)

        width = self.pixmap.width()
        height = self.pixmap.height()

        self.team.setFixedSize(QtCore.QSize(width, height))

        update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)
        self.item_scale.close()

    def right_click_position_scale(self):
        self.position_scale = Menu_Team()
        _translate = QtCore.QCoreApplication.translate
        self.position_scale.setWindowTitle(_translate("MainWindow", "Set position scale"))
        self.position_scale.grb_menu_parameter.setTitle(_translate("MainWindow", "Position Scale"))
        self.position_scale.label_parameter.setText(_translate("MainWindow", "Enter position scale:"))
        self.position_scale.show()

        index = self.index_btn - 1
        position_scale = self.teams_properties[index][2]
        self.position_scale.line_parameter.setText(str(position_scale))

        self.position_scale.btn_ok.clicked.connect(self.right_click_position_scale_ok)  # button OK
        self.position_scale.btn_ok.setAutoDefault(True)

        self.position_scale.btn_cancel.clicked.connect(self.position_scale.menu_cancel)  # button

    def right_click_position_scale_ok(self):
        index = self.index_btn - 1
        itm_scale = float(self.position_scale.line_parameter.displayText())
        self.team = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()

        self.teams_properties[index][2] = itm_scale

        pixmap = QPixmap(self.teams_properties[index][0])
        width = pixmap.width()
        height = pixmap.height()
        self.team.setFixedSize(QtCore.QSize(int(width * itm_scale), int(height * itm_scale)))

        update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)
        self.position_scale.close()

    def right_click_position_offset(self):
        self.position_offset = Position_Offset()
        self.position_offset.show()

        index = self.index_btn - 1
        self.team = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()

        offset_dx = self.teams_properties[index][4]
        offset_dy = self.teams_properties[index][5]

        self.position_offset.label_dX.setText(f'dX ({offset_dx}):')
        self.position_offset.label_dY.setText(f'dY ({offset_dy}):')

        self.position_offset.btn_ok.clicked.connect(self.right_click_position_offset_ok)  # button OK
        self.position_offset.btn_ok.setAutoDefault(True)

        self.position_offset.btn_cancel.clicked.connect(self.position_offset.menu_cancel)  # button Cancel

    def right_click_position_offset_ok(self):
        index = self.index_btn - 1
        self.team = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()

        offset_dx = int(self.position_offset.line_dX.displayText())
        offset_dy = int(self.position_offset.line_dY.displayText())

        self.teams_properties[index][4] += offset_dx
        self.teams_properties[index][5] += offset_dy

        pos_x = self.team.x()
        pos_y = self.team.y()

        self.team.move(pos_x + offset_dx, pos_y + offset_dy)

        update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)
        self.position_offset.close()

    def right_click_remove_team(self):
        self.team = self.v_Layout_frame_items.itemAt(self.index_btn - 1).widget()
        self.select_team.update({self.index_btn: True})
        self.remove_team()

    def load_def_ref(self):
        self.pref = Preference()
        val = read_reference("reference.reg")
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
            if self.player_1 or self.player_2:  # если плеера запущены - ни чего не делает
                pass
        except AttributeError:
            if os.path.isfile(lin_vbg or lin_ibg or lin_vlg):  # если плеера не запущены - проверяет правельность путей
                self.player_1, self.player_2 = start_player()  # запускает плеера
            else:
                self.pref.line_back_video.clear()
                self.pref.line_back_image.clear()
                self.pref.line_logo_video.clear()

        return (self.pref.check_last_session.isChecked(), self.pref.check_box_pause.isChecked(),
                (0, mar_top, 0, mar_bot), ani_dur)

    def create_new(self):

        clear_layout(self.v_Layout_frame_items)
        clear_layout(self.image_rating.v_Layout_grb_items_rat)

        self.teams_properties = []
        self.team_widgets_btn = []
        self.team_widgets_rat = []
        self.select_team.clear()

        self.btn_Remove_Team.setEnabled(False)
        self.btn_Move_to_Pos.setEnabled(False)
        self.btn_Swap_Teams.setEnabled(False)

    def open_file(self, path_op_preset=None):
        try:
            if path_op_preset is None:
                path_op_preset = QFileDialog.getOpenFileNames(self, caption="Open Teams Rating", directory="saves",
                                                              filter="*.sav")[0][0]
            else:
                path_op_preset = path_op_preset

            self.create_new()
            list_str = []
            with open(path_op_preset, "r") as f:
                for line in f.readlines():
                    line1 = ast.literal_eval(line)
                    list_str.append(line1)

            self.teams_properties = list_str

            self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
            self.team_widgets_rat = team_widgets_rat(self.teams_properties, self.image_rating.v_Layout_grb_items_rat)

            val = read_reference("reference.reg")  # считываем параметры margins (top, bottom)
            self.image_rating.v_Layout_grb_items_rat.setContentsMargins(0, val[7], 0, val[8])
            self.image_rating.video.activateWindow()  # делает окно рейтинга активным

        except (IndexError, FileNotFoundError):
            pass

        self.click_team_widget()

    def save_file(self, teams_properties, path_sv_preset=None):
        if path_sv_preset is None:
            path_sv_preset = QFileDialog.getSaveFileName(self, caption="Save Teams Rating", directory="saves",
                                                         filter="*.sav")[0]
        else:
            path_sv_preset = path_sv_preset
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

        self.pref.btn_bg_brow_vid.clicked.connect(self.pref.bg_brow_vid)  # button "Browse..." Background Video file
        self.pref.btn_bg_brow_img.clicked.connect(self.pref.bg_brow_img)  # button "Browse..." Background Image file
        self.pref.btn_lg_brow_vid.clicked.connect(self.pref.lg_brow_vid)  # button "Browse..." Logo Video file

        # TAB COMMON
        self.pref.interface_lang()  # comboBox с выбором языка программы
        val = read_reference("reference.reg")
        self.pref.comboBox_language.setCurrentText(val[11])

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

                update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)

                val = read_reference("reference.reg")  # считываем параметры
                self.on_animation_pause = val[1]
                self.contents_margin = self.image_rating.v_Layout_grb_items_rat.setContentsMargins(0, val[7], 0, val[8])
                self.animation_duration = val[9]

                self.image_rating.video.activateWindow()  # делает окно рейтинга активным

            if self.logo_or_rating == 1:  # если кнопка Logo/Rating была в положение Logo меняет на Rating
                self.logo_or_rating -= 1
                self.btn_Logo_Rating.setChecked(False)
                # _translate = QtCore.QCoreApplication.translate
                # self.btn_Logo_Rating.setText(_translate("MainWindow", "R A T I N G"))
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

        self.add_team.btn_brow_image.clicked.connect(self.add_team.add_team_brow_img)  # Item Image "Browse..."

        self.add_team.btn_ok.clicked.connect(self.add_new_team_ok)  # button OK
        self.add_team.btn_ok.setAutoDefault(True)

        self.add_team.btn_cancel.clicked.connect(self.add_team.add_cancel)  # button

    def add_new_team_ok(self):
        if self.add_team.line_image.displayText() and self.add_team.line_text.displayText():
            prop = [self.add_team.line_image.displayText(),
                    self.add_team.line_text.displayText(), 1.0, 1.0, 0, 0]
            index = str(self.v_Layout_frame_items.count() + 1)

            self.teams_properties += [prop]

            self.team = Widget_Team_Button(index, self.add_team.line_text.displayText())
            self.v_Layout_frame_items.addWidget(self.team)

            self.team_rat = Widget_Team_Rating(self.add_team.line_image.displayText())
            scale = float(self.teams_properties[int(index) - 1][2])
            pixmap = QPixmap(self.teams_properties[int(index) - 1][0])
            width = pixmap.width()
            height = pixmap.height()
            self.team_rat.setFixedSize(QtCore.QSize(int(width * scale), int(height * scale)))
            self.image_rating.v_Layout_grb_items_rat.addWidget(self.team_rat, 0, QtCore.Qt.AlignHCenter)

            self.add_team.close()

            self.team_widgets_btn.append(self.team)  # список виджетов команд с кнопками
            self.team_widgets_rat.append(self.team_rat)  # список виджетов команд с банерами

            update_layout(1, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat, self.teams_properties)

            val = read_reference("reference.reg")  # считываем параметры margins (top, bottom)
            self.image_rating.v_Layout_grb_items_rat.setContentsMargins(0, val[7], 0, val[8])
            self.image_rating.video.activateWindow()  # делает окно рейтинга активным

            self.click_team_widget()

    def remove_team(self):
        pos = list(self.select_team.keys())
        pos.sort(reverse=True)
        for i in pos:
            self.team_widgets_btn.pop(i - 1)
            self.team_widgets_rat.pop(i - 1)

            self.teams_properties.pop(i - 1)

            team_btn = self.v_Layout_frame_items.itemAt(i - 1).widget()  # удаляет виджет с кнопкой
            self.v_Layout_frame_items.removeWidget(team_btn)

            team_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(i - 1).widget()  # удаляет виджет с банером
            team_rat.deleteLater()
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

    def swap_teams(self):
        pos = list(self.select_team.keys())
        pos.sort(reverse=True)
        index_1, index_2 = pos  # инедксы виджетов выбраных для перемещения

        team_1_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(index_1 - 1).widget()
        team_2_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(index_2 - 1).widget()
        # team_1_rat.raise_()
        # team_2_rat.lower()
        width_1 = self.image_rating.v_Layout_grb_items_rat.itemAt(index_1 - 1).widget().width()
        width_2 = self.image_rating.v_Layout_grb_items_rat.itemAt(index_2 - 1).widget().width()
        height_1 = self.image_rating.v_Layout_grb_items_rat.itemAt(index_1 - 1).widget().height()
        height_2 = self.image_rating.v_Layout_grb_items_rat.itemAt(index_2 - 1).widget().height()

        x_1, x_2, scale = int(width_1 / 2), int(width_2 / 2), int(height_1 - height_2)

        off_x_1 = self.teams_properties[index_1 - 1][4]
        off_x_2 = self.teams_properties[index_2 - 1][4]

        self.anim_group_1 = QParallelAnimationGroup()

        self.anim_1 = QPropertyAnimation(team_1_rat, b"pos", self)  # back down
        self.anim_1.setKeyValueAt(0, QPoint(960 + off_x_1 - x_1, team_1_rat.y()))
        # self.anim_1.setKeyValueAt(0.5, QPoint(
        #     int((960 + off_x_2) - x_1 * 1.3), int(team_2_rat.y() - ((team_2_rat.y() - team_1_rat.y()) / 2))))
        self.anim_1.setKeyValueAt(1, QPoint(960 + off_x_2 - x_1, team_2_rat.y()))
        self.anim_1.setEasingCurve(QEasingCurve.InOutCirc)
        self.anim_1.setDuration(self.animation_duration)
        self.anim_group_1.addAnimation(self.anim_1)

        self.anim_2 = QPropertyAnimation(team_2_rat, b"pos", self)  # front up
        self.anim_2.setKeyValueAt(0, QPoint(960 + off_x_2 - x_2, team_2_rat.y()))
        # self.anim_2.setKeyValueAt(0.5, QPoint(
        #     int((960 + off_x_1) - x_2 / 1.3), int(team_1_rat.y() + scale - ((team_1_rat.y() - team_2_rat.y()) / 2))))
        self.anim_2.setKeyValueAt(1, QPoint(960 + off_x_1 - x_2, int(team_1_rat.y() + scale)))
        self.anim_2.setEasingCurve(QEasingCurve.InOutCirc)
        self.anim_2.setDuration(self.animation_duration)
        self.anim_group_1.addAnimation(self.anim_2)

        self.anim_3 = QPropertyAnimation(team_1_rat, b"size", self)  # back down
        self.anim_3.setKeyValueAt(0, QSize(width_1, height_1))
        self.anim_3.setKeyValueAt(0.5, QSize(int(width_1 * 1.3), int(height_1 * 1.3)))
        self.anim_3.setKeyValueAt(1, QSize(width_1, height_1))
        self.anim_3.setEasingCurve(QEasingCurve.InOutCirc)
        self.anim_3.setDuration(self.animation_duration)
        self.anim_group_1.addAnimation(self.anim_3)

        self.anim_4 = QPropertyAnimation(team_2_rat, b"size", self)  # front up
        self.anim_4.setKeyValueAt(0, QSize(width_2, height_2))
        self.anim_4.setKeyValueAt(0.5, QSize(int(width_2 / 1.3), int(height_2 / 1.3)))
        self.anim_4.setKeyValueAt(1, QSize(width_2, height_2))
        self.anim_4.setEasingCurve(QEasingCurve.InOutCirc)
        self.anim_4.setDuration(self.animation_duration)
        self.anim_group_1.addAnimation(self.anim_4)

        self.anim_group_2 = QParallelAnimationGroup()
        i = index_1 - 2
        while i >= index_2:
            team_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget()
            self.anim = QPropertyAnimation(team_rat, b"pos")
            x_l, y_l = team_rat.x(), team_rat.y()
            self.anim.setKeyValueAt(0, QPoint(x_l, y_l))
            self.anim.setKeyValueAt(1, QPoint(x_l, y_l + scale))
            i -= 1
            self.anim.setEasingCurve(QEasingCurve.Linear)
            self.anim.setDuration(self.animation_duration)
            self.anim_group_2.addAnimation(self.anim)

        if self.on_animation_pause:
            self.player_1.pause()
            QTimer.singleShot(self.animation_duration, self.player_1.player.play)
        self.btn_Swap_Teams.setEnabled(False)
        QTimer.singleShot(self.animation_duration, lambda: self.btn_Swap_Teams.setEnabled(True))

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_group_1)
        self.anim_group.addAnimation(self.anim_group_2)

        self.anim_group.start()

        team_w_btn = self.team_widgets_btn.pop(index_1 - 1)
        self.team_widgets_btn.insert(index_2 - 1, team_w_btn)
        team_w_rat = self.team_widgets_rat.pop(index_1 - 1)
        self.team_widgets_rat.insert(index_2 - 1, team_w_rat)

        team_p1_1 = self.teams_properties.pop(index_1 - 1)
        team_p2_1 = self.teams_properties.pop(index_2 - 1)

        self.teams_properties.insert(index_2 - 1, team_p1_1)
        self.teams_properties.insert(index_1 - 1, team_p2_1)

        clear_layout(self.v_Layout_frame_items)
        self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)
        #
        for b in range(self.image_rating.v_Layout_grb_items_rat.count()):
            w = 960 - int(self.image_rating.v_Layout_grb_items_rat.itemAt(b).widget().width() / 2)
            self.teams_properties[b][4] = self.image_rating.v_Layout_grb_items_rat.itemAt(b).widget().x() - w

        update_layout(self.animation_duration, self.image_rating.v_Layout_grb_items_rat, self.team_widgets_rat,
                      self.teams_properties)

        team_1_btn = self.v_Layout_frame_items.itemAt(index_1 - 1).widget()
        team_2_btn = self.v_Layout_frame_items.itemAt(index_2 - 1).widget()
        team_1_btn.btn_Team.setChecked(True)
        team_2_btn.btn_Team.setChecked(True)

        self.lineEdit_Pos.setText("")

        self.click_team_widget()

    def move_team(self):
        index = list(self.select_team.keys())[0] - 1  # инедкс виджета выбраного для перемещения
        try:
            position = int(self.lineEdit_Pos.displayText()) - 1  # номер позиции куда перемещаем виджет
            if 0 <= position <= self.v_Layout_frame_items.count():
                try:
                    team_1_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget()
                    width, height = team_1_rat.width(), team_1_rat.height()
                    team_1_rat.raise_()
                    team_2_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(position).widget()
                    x_1 = int(self.image_rating.v_Layout_grb_items_rat.itemAt(index).widget().width() / 2)
                    off_x_1 = self.teams_properties[index][4]
                    off_x_2 = self.teams_properties[position][4]

                    self.anim_1 = QPropertyAnimation(team_1_rat, b"pos")
                    self.anim_1.setKeyValueAt(0, QPoint(960 + off_x_1 - x_1, team_1_rat.y()))
                    self.anim_1.setEasingCurve(QEasingCurve.InOutExpo)
                    self.anim_1.setDuration(self.animation_duration)

                    self.anim_group = QParallelAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)

                    x, y, off_x = team_1_rat.x(), team_1_rat.y(), off_x_1
                    scale = team_1_rat.height()
                    if position <= index:  # up
                        self.anim_1.setKeyValueAt(1, QPoint(960 + off_x_2 - x_1, team_2_rat.y()))
                        i = index - 1
                        while i >= position:
                            team_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget()
                            w = int(self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget().width() / 2)
                            s = int(self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget().height()) - scale
                            self.anim_2 = QPropertyAnimation(team_rat, b"pos")
                            x_i, y_i = team_rat.x(), team_rat.y()
                            self.anim_2.setKeyValueAt(0, QPoint(x_i, y_i))
                            self.anim_2.setKeyValueAt(1, QPoint(960 + off_x - w, y - s))
                            x, y, off_x = x_i, y_i, self.teams_properties[i][4]
                            i -= 1
                            self.anim_2.setEasingCurve(QEasingCurve.InOutExpo)
                            self.anim_2.setDuration(self.animation_duration)
                            self.anim_group.addAnimation(self.anim_2)

                    elif position < self.v_Layout_frame_items.count():  # down
                        self.anim_1.setKeyValueAt(1, QPoint(960 + off_x_2 - x_1, team_2_rat.y() -
                                                            (team_1_rat.height() - team_2_rat.height())))
                        i = index + 1
                        while i <= position:
                            team_rat = self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget()
                            w = int(self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget().width() / 2)
                            s = scale - int(self.image_rating.v_Layout_grb_items_rat.itemAt(i).widget().height())
                            self.anim_2 = QPropertyAnimation(team_rat, b"pos")
                            x_i, y_i = team_rat.x(), team_rat.y()
                            self.anim_2.setKeyValueAt(0, QPoint(x_i, y_i))
                            self.anim_2.setKeyValueAt(1, QPoint(960 + off_x - w, y))
                            x, y, off_x = x_i, y_i - s, self.teams_properties[i][4]
                            i += 1
                            self.anim_2.setEasingCurve(QEasingCurve.InOutExpo)
                            self.anim_2.setDuration(self.animation_duration)
                            self.anim_group.addAnimation(self.anim_2)

                    self.anim_3 = QPropertyAnimation(team_1_rat, b"size", self)  # back down
                    self.anim_3.setKeyValueAt(0, QSize(width, height))
                    self.anim_3.setKeyValueAt(0.5, QSize(int(width * 1.3), int(height * 1.3)))
                    self.anim_3.setKeyValueAt(1, QSize(width, height))
                    self.anim_3.setEasingCurve(QEasingCurve.InOutCirc)
                    self.anim_3.setDuration(self.animation_duration)
                    self.anim_group.addAnimation(self.anim_3)

                    if self.on_animation_pause:
                        self.player_1.pause()
                        QTimer.singleShot(self.animation_duration, self.player_1.player.play)
                    self.btn_Move_to_Pos.setEnabled(False)
                    QTimer.singleShot(self.animation_duration, lambda: self.btn_Move_to_Pos.setEnabled(True))

                    self.anim_group.start()

                    team_w_btn = self.team_widgets_btn.pop(index)
                    self.team_widgets_btn.insert(position, team_w_btn)
                    team_w_rat = self.team_widgets_rat.pop(index)
                    self.team_widgets_rat.insert(position, team_w_rat)

                    team_p1 = self.teams_properties.pop(index)
                    self.teams_properties.insert(position, team_p1)

                    clear_layout(self.v_Layout_frame_items)
                    self.team_widgets_btn = team_widgets(self.teams_properties, self.v_Layout_frame_items)

                    for b in range(self.image_rating.v_Layout_grb_items_rat.count()):
                        w = 960 - int(self.image_rating.v_Layout_grb_items_rat.itemAt(b).widget().width() / 2)
                        self.teams_properties[b][4] = self.image_rating.v_Layout_grb_items_rat.itemAt(
                            b).widget().x() - w

                    update_layout(self.animation_duration, self.image_rating.v_Layout_grb_items_rat,
                                  self.team_widgets_rat, self.teams_properties)

                    self.select_team.clear()

                    team_2 = self.v_Layout_frame_items.itemAt(position).widget()
                    team_2.btn_Team.setChecked(True)
                    self.select_team[position + 1] = True
                except AttributeError:
                    pass

                self.lineEdit_Pos.setText("")
            self.click_team_widget()
        except ValueError:
            pass

    def logo_rating(self):
        try:
            if self.player_1 and self.player_2:
                if self.logo_or_rating == 0:
                    self.player_2.video.activateWindow()
                    self.logo_or_rating += 1
                    _translate = QtCore.QCoreApplication.translate
                    self.btn_Logo_Rating.setText(_translate("MainWindow", "L O G O"))
                elif self.logo_or_rating == 1:
                    self.player_1.video.activateWindow()
                    self.image_rating.video.activateWindow()
                    self.logo_or_rating -= 1
                    _translate = QtCore.QCoreApplication.translate
                    self.btn_Logo_Rating.setText(_translate("MainWindow", "R A T I N G"))
        except AttributeError:
            pass

    def closeEvent(self, event):
        self.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    file_lng = read_reference("reference.reg")
    language = file_lng[11]

    translator = QTranslator()
    translator.load("./lang/" + language)
    if not app.installTranslator(translator):
        pass

    windows = MainRATING()
    windows.show()
    sys.exit(app.exec_())
