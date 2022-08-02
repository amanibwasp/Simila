import pygame

class General_room_books():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.image_active = pygame.image.load("Images/books_active.png")
        self.image_inactive = pygame.image.load("Images/books_inactive.png")
        self.rect = self.image_inactive.get_rect()
        self.rect.centery = self.screenObject.screen_rect[3] - 650
        self.rect.centerx = self.screenObject.screen_rect.centerx

    def books_active_output(self):
        self.screenObject.screen.blit(self.image_active, self.rect)

    def books_inactive_output(self):
        self.screenObject.screen.blit(self.image_inactive, self.rect)

    def option(self):
        self.click = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        if self.rect.left + 331 <= self.mouse_pos[0] <= self.rect.left + 350 and self.rect.top + 120 <= self.mouse_pos[1] <= self.rect.top + 120 + 63:
            self.books_active_output()
        else:
            self.books_inactive_output()
