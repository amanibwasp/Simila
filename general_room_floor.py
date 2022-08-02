import pygame

class General_room_floor():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.image = pygame.image.load("Images/floor.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screenObject.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def floor_output(self):
        self.screenObject.screen.blit(self.image, self.rect)