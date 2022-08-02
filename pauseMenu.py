import pygame
class PauseMenu():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.background_image = pygame.image.load('Images/pause_menu/background.png')
        self.resume_button_active_image = pygame.image.load('Images/pause_menu/resume_button_active.png')
        self.resume_button_inactive_image = pygame.image.load('Images/pause_menu/resume_button_inactive.png')
        self.exit_button_active_image = pygame.image.load('Images/pause_menu/exit_button_active.png')
        self.exit_button_active_image = pygame.image.load('Images/pause_menu/exit_button_inactive.png')
        self.logo_image = pygame.image.load('Images/Logo.png')
        self.paused = False

        self.background_image_rect = self.background_image.get_rect()
        self.logo_image_rect = self.logo_image.get_rect()
        self.resume_button_active_image_rect = self.resume_button_active_image.get_rect()
        self.exit_button_active_image_rect = self.exit_button_active_image.get_rect()

        self.background_image_rect.centerx = self.screenObject.screen_rect.centerx
        self.background_image_rect.centery = self.screenObject.screen_rect.centery

        self.screenObject = screenObject

    def check_for_pause(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.paused = True
                self.get_paused()

    def get_paused(self):
        print('got paused')
        while self.paused:
            print('again')
           #self.screenObject.screen.fill((0,0,0)) #ЗАЛИВКА ВЫПОЛНЯЕТСЯ ПОСЛЕДНЕЙ, ТАК ЧТО ЧЕК НА ПАУЗУ В ВАЙЛАХ В ПОСЛЕДНЮЮ ОЧЕРЕДЬ
           # self.screenObject.screen.blit(self.background_image, self.background_image_rect)


