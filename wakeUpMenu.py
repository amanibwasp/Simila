import pygame
import controls
from dialog import Dialog
from mouse_control import Mouse_control
from generalMenu import GeneralMenu

class WakeUpMenu:
    def __init__(self, screenObject):
        self.wake_up_menu_running = True
        self.dialog = Dialog(screenObject) #получаем доступ ко всем диалоговым окнам
        self.dialog.dialog_phase = 'where'
        self.screenObject = screenObject
        self.mouse_control = Mouse_control()
        self.run_window()

    def kill_menu(self):
        self.wake_up_menu_running = False

    def run_window(self):
        while self.wake_up_menu_running:
            self.screenObject.screen.fill((0, 0, 0))
            self.mouse_control.pos_and_click_for_dialog(self.dialog, self.general_menu_start)
            self.dialog.update_dialog()
            controls.update_screen()

    def general_menu_start(self):
        gm = GeneralMenu(self.screenObject)
        self.kill_menu()


