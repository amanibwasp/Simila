import pygame

class General_room_table():
    def __init__(self, screenObject):
        self.image_active = pygame.image.load("Images/table_active.png")
        self.image_inactive = pygame.image.load("Images/table_inactive.png")
        self.rect = self.image_inactive.get_rect()
        self.screenObject = screenObject
        self.rect.centerx = self.screenObject.screen_rect[2] // 4
        self.rect.y = self.screenObject.screen_rect[3] - 282

    def table_active_output(self):
        self.screenObject.screen.blit(self.image_active, self.rect)

    def table_inactive_output(self):
        self.screenObject.screen.blit(self.image_inactive, self.rect)

    def option(self, action):
        self.action = action
        self.click = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        if self.rect.x + 27 <= self.mouse_pos[0] <= self.rect.x + 27 + 113 and 96 + self.rect.y <= self.mouse_pos[1] <= 96 + 32 + self.rect.y:
            self.table_active_output()
            if self.click[0]:
                self.action()
        else:
            self.table_inactive_output()
