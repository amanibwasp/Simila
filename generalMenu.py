
import pygame
import controls
from dialog import Dialog
from simila import Simila
from simila_dialogs import Simila_dialogs
from mouse_control import Mouse_control
from general_room_floor import General_room_floor
from general_room_door import General_room_door
from general_room_table import General_room_table
from general_room_pk import General_room_pk
from general_room_books import General_room_books
class GeneralMenu():
    def __init__(self, screenObject):
        pygame.time.delay(300)
        self.screenObject = screenObject
        self.general_room_floor = General_room_floor(self.screenObject)
        self.general_room_door = General_room_door(self.screenObject)
        self.dialog = Dialog(self.screenObject)
        self.dialog.dialog_phase = 'general_room_greetings'
        self.simila = Simila(self.screenObject)
        self.simila_dialogs = Simila_dialogs(self.screenObject, self.simila, self)
        self.mouse_control = Mouse_control()
        self.general_room_table = General_room_table(self.screenObject)
        self.general_room_pk = General_room_pk(self.screenObject)
        self.general_room_books = General_room_books(self.screenObject)
        self.general_menu_running = True
        self.general_room_pk_close_running = False

        self.bg_color = (186,144,69)
        self.run_window()

    def run_window(self):
        while self.general_menu_running:
            controls.update_screen()
            self.screenObject.screen.fill(self.bg_color)
            self.general_room_floor.floor_output()
            self.general_room_door.option(self.general_room_door_close)
            self.general_room_table.option()
            self.general_room_pk.option(self.general_room_pk_close)
            self.general_room_books.option()
            self.dialog.update_dialog()
            self.mouse_control.pos_and_click_for_dialog(self.dialog, self.dialog.kill_dialog)

    def kill_menu(self):
        self.general_menu_running = False

    def revive_menu(self):
        self.general_menu_running = True

    def general_room_door_close(self):
        self.kill_menu()
        self.general_room_door_close_image = pygame.image.load('Images/closed_door.png')
        self.rect_general_room_door_close_image = self.general_room_door_close_image.get_rect()
        self.rect_general_room_door_close_image.centerx = self.screenObject.screen_rect.centerx
        self.rect_general_room_door_close_image.centery = self.screenObject.screen_rect.centery
        self.back_inactive_image = pygame.image.load('Images/back_inactive.png')
        self.back_active_image = pygame.image.load('Images/back_active.png')
        self.back_rect = self.back_active_image.get_rect()
        self.back_rect.right = self.screenObject.screen_rect.right
        self.back_rect.bottom = self.screenObject.screen_rect.bottom
        self.general_room_door_close_running = True
        while self.general_room_door_close_running:
            controls.update_screen()
            self.screenObject.screen.fill((161,161,161))
            self.mouse_pos = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.screenObject.screen.blit(self.general_room_door_close_image, self.rect_general_room_door_close_image)
            if self.back_rect.left <= self.mouse_pos[0] <= self.back_rect.right and self.back_rect.top <= self.mouse_pos[1] <= self.back_rect.bottom:
                self.screenObject.screen.blit(self.back_active_image, self.back_rect)
                if self.click[0]:
                    self.revive_menu()
                    self.general_room_door_close_running = False
            else:
                self.screenObject.screen.blit(self.back_inactive_image, self.back_rect)
    def general_room_pk_close(self):
        self.kill_menu()
        self.short_info_image = pygame.image.load('Images/pk_close/short_info.png')
        self.suspicious_image = pygame.image.load('Images/pk_close/suspicious.png')
        self.suspicious_prohibited_image = pygame.image.load('Images/pk_close/suspicious_prohibited.png')
        self.back_inactive_image = pygame.image.load('Images/back_inactive.png')
        self.back_active_image = pygame.image.load('Images/back_active.png')
        self.back_rect = self.back_active_image.get_rect()
        self.back_rect.bottom = self.screenObject.screen_rect.bottom
        self.back_rect.right = self.screenObject.screen_rect.right
        self.short_info_image_rect = self.short_info_image.get_rect()
        self.suspicious_image_rect = self.suspicious_image.get_rect()
        self.general_room_pk_close_running = True
        self.short_info_image_rect.right = self.screenObject.screen_rect.right-50
        self.short_info_image_rect.top = self.screenObject.screen_rect.top
        self.suspicious_image_rect.centerx = self.screenObject.screen_rect.centerx
        self.suspicious_image_rect.centery = self.screenObject.screen_rect.centery
        while self.general_room_pk_close_running:
            controls.update_screen()
            self.screenObject.screen.fill((119,215,245))
            self.mouse_pos = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            if self.simila.state == None:
                self.screenObject.screen.blit(self.short_info_image, self.short_info_image_rect)

            # проверка Симилы на состояние и последующее размещение в зависимости от диалога
            if self.simila_dialogs.run_dialog or self.dialog.dialog_phase != None:
                self.simila.simila_rect.bottom = self.simila_dialogs.dialog_rect.top
                self.simila.simila_rect.centerx = self.simila_dialogs.dialog_rect.centerx
            else:
                self.simila.simila_rect.bottom = self.screenObject.screen_rect.bottom
                self.simila.simila_rect.centerx = self.screenObject.screen_rect.centerx
            self.simila.output_simila()

            #ПОДОЗРИТЕЛЬНЫЙ ФАЙЛ
            if self.simila.state == None:
                if self.suspicious_image_rect.left <= self.mouse_pos[0] <= self.suspicious_image_rect.right and self.suspicious_image_rect.top <= self.mouse_pos[1] <= self.suspicious_image_rect.bottom:
                    self.screenObject.screen.blit(self.suspicious_prohibited_image, self.suspicious_image_rect)
                    if self.click[0]:
                        self.simila.state = 'happy'
                        self.dialog.dialog_phase = 'simila_greetings'
                else:
                    self.screenObject.screen.blit(self.suspicious_image, self.suspicious_image_rect)

            #КНОПКА НАЗАД
            if self.back_rect.left <= self.mouse_pos[0] <= self.back_rect.right and self.back_rect.top <= self.mouse_pos[1] <= self.back_rect.bottom:
                self.screenObject.screen.blit(self.back_active_image, self.back_rect)
                if self.click[0]:
                    self.revive_menu()
                    self.dialog.kill_dialog()
                    self.simila.state = None
                    self.general_room_pk_close_running = False
            else:
                self.screenObject.screen.blit(self.back_inactive_image, self.back_rect)

            #ПРОКРУЧИВАНИЕ ДИАЛОГОВ С СИМИЛОЙ:
            if self.simila_dialogs.run_dialog:
                self.simila_dialogs.check_mouse_pos_for_options()
                self.simila_dialogs.if_clicked()
                self.simila_dialogs.run_simila_dialog()
            self.mouse_control.pos_and_click_for_dialog(self.dialog)
            self.dialog.update_dialog()



