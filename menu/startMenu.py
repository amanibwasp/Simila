import pygame
import common_settings.controls as controls
from objects.startBtn import StartBtn
from menu.wakeUpMenu import  WakeUpMenu


class StartMenu():
    def __init__(self, screenObject):
        self.start_menu_running = True
        self.screenObject = screenObject
        self.startBtn = StartBtn(screenObject, self.wake_up_menu_start)
        self.logo_image = pygame.image.load('Images/game/logo.png')
        self.logo_image_rect = self.logo_image.get_rect()
        self.logo_image_rect.top = self.screenObject.screen_rect.top + 50
        self.logo_image_rect.centerx = self.screenObject.screen_rect.centerx
        self.run_window()

    def kill_menu(self):
        self.start_menu_running = False

    def run_window(self):
        while self.start_menu_running:
            self.screenObject.screen.fill((65, 133, 190))
            self.startBtn.option()
            self.screenObject.screen.blit(self.logo_image, self.logo_image_rect)
            controls.update_screen()

    def wake_up_menu_start(self):
        pygame.time.delay(300)
        wum = WakeUpMenu(self.screenObject)
        self.kill_menu()
