import pygame
class General_room_door():
    def __init__(self, screenObject):
        self.image_active = pygame.image.load("Images/door_active.png")
        self.image_inactive = pygame.image.load("Images/door_inactive.png")
        self.rect = self.image_active.get_rect()
        self.screenObject = screenObject
        self.rect.bottom = self.screenObject.screen_rect[3] - 82
        self.rect.x = self.screenObject.screen_rect[2] // 1.5

    def door_active_output(self):
        self.screenObject.screen.blit(self.image_active, self.rect)
    def door_inactive_output(self):
        self.screenObject.screen.blit(self.image_inactive, self.rect)

    def option(self, action):
        self.action = action
        self.mouse_pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.rect.left <= self.mouse_pos[0] <= self.rect.right and self.rect.top <= self.mouse_pos[1] <= self.rect.bottom:
            self.door_active_output()
            if self.click[0]:
                pygame.time.delay(100)
                self.action()
        else:
            self.door_inactive_output()
