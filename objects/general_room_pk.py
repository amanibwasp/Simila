import pygame


class General_room_pk():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.image_active = pygame.image.load("Images/game/pk_active.png")
        self.image_inactive = pygame.image.load("Images/game/pk_inactive.png")
        self.rect = self.image_inactive.get_rect()
        self.rect.y = self.screenObject.screen_rect[3] - 82 - 135 - 200
        self.rect.centerx = self.screenObject.screen_rect[2] // 4

    def pk_active_output(self):
        self.screenObject.screen.blit(self.image_active, self.rect)

    def pk_inactive_output(self):
        self.screenObject.screen.blit(self.image_inactive, self.rect)

    def option(self, action):
        self.action = action
        self.click = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        if self.rect.left <= self.mouse_pos[0] <= self.rect.right and self.rect.top <= self.mouse_pos[
            1] <= self.rect.bottom:
            self.pk_active_output()
            if self.click[0]:
                action()
        else:
            self.pk_inactive_output()
