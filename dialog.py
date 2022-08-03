import pygame
class Dialog():
    #данный класс позволяет получить доступ ко всем диалоговым окнам и методам их размещения
    #то есть атрибут этого класса - по сути все диалоговые окна и ещё и функция в добавок
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.image_dialog = pygame.image.load("Images/dialog.png")
        self.image_dialog_where = pygame.image.load("Images/where.png")
        self.image_dialog_observe = pygame.image.load("Images/observe.png")
        self.image_dialog_general_room_greetings = pygame.image.load("Images/general_room_greetings.png")
        self.rect = self.image_dialog_where.get_rect()
        self.screen_rect = screenObject.screen.get_rect() #опять недурно сработал, молодец "я" из прошлого
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.dialog_phase = None

    def place_dialog(self):
        self.screenObject.screen.blit(self.image_dialog, self.rect)

    def kill_dialog(self):
        self.dialog_phase = None

    def update_dialog(self):
        match self.dialog_phase:
            case 'where': self.screenObject.screen.blit(self.image_dialog_where, self.rect)
            case 'observe': self.screenObject.screen.blit(self.image_dialog_observe, self.rect)
            case 'general_room_greetings': self.screenObject.screen.blit(self.image_dialog_general_room_greetings, self.rect)

        

