import pygame

class StartBtn():
    def __init__(self, screenObject, action):
        self.action = action
        self.screen = screenObject.screen
        self.screen_rect = screenObject.screen.get_rect()
        self.image= pygame.image.load("Images/startbtn.png")
        self.image_active = pygame.image.load("Images/startbtn_active.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    #рисование неактивной кнопки старта
    def output_inactive(self):
        self.screen.blit(self.image, self.rect)
    #рисование активной кнопки старта
    def output_active(self):
        self.screen.blit(self.image_active, self.rect)
    #ОСНОВНОЙ МЕТОД ОТОБРАЖЕНИЯ КНОПКИ
    def option(self):
        click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        if self.rect.left <= self.mouse[0] <= self.rect.right and self.rect.top <= self.mouse[1] <= self.rect.bottom:
            self.output_active()
            if click[0]:
                self.action()
                pygame.time.delay(300)
        else:
            self.output_inactive()


