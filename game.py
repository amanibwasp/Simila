import sys
import pygame
class Game():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.bg_active_image = pygame.image.load('Images/game/bg_active.png')
        self.bg_inactive_image = pygame.image.load('Images/game/bg_inactive.png')
        self.bg_images = [pygame.image.load('Images/game/bg_active.png'), pygame.image.load('Images/game/bg_inactive.png')]
        self.bg_number = 0
        self.bg_rect = self.bg_active_image.get_rect()
        self.bg_rect.centerx = self.screenObject.screen_rect.centerx
        self.bg_rect.centery = self.screenObject.screen_rect.centery
        self.moveLeft = [pygame.image.load('Images/game/unknown_left_1.png'), pygame.image.load('Images/game/unknown_left_2.png')]
        self.unknown_standing = pygame.image.load('Images/game/unknown_0.png')
        self.moveRight = [pygame.image.load('Images/game/unknown_right_1.png'), pygame.image.load('Images/game/unknown_right_2.png')]
        self.speed = 6
        self.clock = pygame.time.Clock()
        self.animCnt = 0
        self.right = False
        self.left = False
        self.unknown_rect = self.unknown_standing.get_rect()
        self.unknown_rect.centerx = self.bg_rect.centerx
        self.unknown_rect.bottom = self.bg_rect.bottom - 15
        pygame.time.set_timer(pygame.USEREVENT, 2000)

    def run_game(self):
        while True:
            self.clock.tick(30)
            self.screenObject.screen.fill((0,0,0))
            self.screenObject.screen.blit(self.bg_images[self.bg_number], self.bg_rect)
            self.check_pressed_btn()
            self.move_unknown()
            self.place_unknown()
            pygame.display.flip()

    def check_pressed_btn(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.right = True
                    self.left = False
                elif event.key == pygame.K_a:
                    self.left = True
                    self.right = False
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.right = False
                elif event.key == pygame.K_a:
                    self.left = False
            elif event.type == pygame.USEREVENT:
                if self.bg_number == 0:
                    self.bg_number += 1
                else:
                    self.bg_number -= 1
    def move_unknown(self):
        if self.right and self.unknown_rect.right <= self.bg_rect.right - 25:
            self.unknown_rect.centerx += self.speed
            self.animCnt += 1
        elif self.left and self.unknown_rect.left > self.bg_rect.left + 25:
            self.unknown_rect.centerx -= self.speed
            self.animCnt += 1

    def place_unknown(self):
        if self.animCnt >= 29:
            self.animCnt = 0
        if self.left:
            self.screenObject.screen.blit(self.moveLeft[self.animCnt//15], self.unknown_rect)
        elif self.right:
            self.screenObject.screen.blit(self.moveRight[self.animCnt//15], self.unknown_rect)
        else:
            self.screenObject.screen.blit(self.unknown_standing, self.unknown_rect)



