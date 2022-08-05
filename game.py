import sys
import pygame
from random import randint
from pygame.sprite import Group
from pygame.sprite import Group
class Game():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.bg_active_image = pygame.image.load('Images/game/bg_active.png')
        self.bg_inactive_image = pygame.image.load('Images/game/bg_inactive.png')
        self.bg_images = [pygame.image.load('Images/game/bg_active.png'), pygame.image.load('Images/game/bg_inactive.png')]
        self.bg_game_over_image = pygame.image.load('Images/game/game_over.png')

        #ВРЕМЕННЫЙ ЭКРАН ПОБЕДЫ ----------------------
        self.vic_im = pygame.image.load('Images/game/vic.png')
        self.vic_rect = self.vic_im.get_rect()
        self.vic_rect.centerx = self.screenObject.screen_rect.centerx
        self.vic_rect.centery = self.screenObject.screen_rect.centery
        self.vic = False
        #ВРЕМЕННЫЙ ЭКРАН ПОБЕДЫ ----------------------

        self.bg_game_over_rect = self.bg_game_over_image.get_rect()
        self.bg_number = 0
        self.bg_rect = self.bg_active_image.get_rect()
        self.bg_rect.centerx = self.screenObject.screen_rect.centerx
        self.bg_rect.centery = self.screenObject.screen_rect.centery
        self.bg_game_over_rect.centerx = self.screenObject.screen_rect.centerx
        self.bg_game_over_rect.centery = self.screenObject.screen_rect.centery
        self.unknown = Unknown(self.bg_rect, self.screenObject)
        self.clock = pygame.time.Clock()
        self.arrows = Group()
        self.game_over = False
        self.game_running = True

    def run_game(self):
        self.set_timers()
        while self.game_running:
            self.clock.tick(30)
            self.screenObject.screen.fill((0,0,0))
            self.screenObject.screen.blit(self.bg_images[self.bg_number], self.bg_rect)
            self.check_pressed_btn()
            self.unknown.move_unknown()
            self.unknown.place_unknown()
            for arrow in self.arrows.sprites():
                arrow.draw_arrow()
            self.arrows.update()
            for arrow in self.arrows.copy():
                if arrow.rect.bottom >= self.bg_rect.bottom - 15:
                    self.arrows.remove(arrow)
            if pygame.sprite.spritecollideany(self.unknown, self.arrows):
                self.game_running = False
                self.game_over = True
            pygame.display.flip()
        while self.game_over:
            self.screenObject.screen.blit(self.bg_game_over_image, self.bg_game_over_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            pygame.display.flip()
        while self.vic:
            self.screenObject.screen.blit(self.vic_im, self.vic_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            pygame.display.flip()

    def set_timers(self):
        pygame.time.set_timer(pygame.USEREVENT, 500) #для обновления бг
        pygame.time.set_timer(123, 300) #123 - номер таймера на появление стрел
        pygame.time.set_timer(124, 30000, 1) #124 - номер таймера до победы

    def check_pressed_btn(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.unknown.right = True
                    self.unknown.left = False
                elif event.key == pygame.K_a:
                    self.unknown.left = True
                    self.unknown.right = False
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.unknown.right = False
                elif event.key == pygame.K_a:
                    self.unknown.left = False
            elif event.type == pygame.USEREVENT:
                if self.bg_number == 0:
                    self.bg_number += 1
                else:
                    self.bg_number -= 1
            elif event.type == 123:
                arrow = Arrow(self.bg_rect, self.screenObject)
                self.arrows.add(arrow)
            elif event.type == 124:
                self.game_running = False
                self.vic = True



class Arrow(pygame.sprite.Sprite):
    def __init__(self, bg_rect, screenObject):
        super(Arrow, self).__init__()
        self.screenObject = screenObject
        self.bg_rect = bg_rect
        self.arrow_image = pygame.image.load('Images/game/arrow.png')
        self.rect = self.arrow_image.get_rect()
        self.rect.top = self.bg_rect.top
        self.rect.centerx = randint(self.bg_rect.left + 30, self.bg_rect.right - 30)
        self.speed = 12

    def update(self):
        self.rect.y += self.speed


    def draw_arrow(self):
        self.screenObject.screen.blit(self.arrow_image, self.rect)

class Unknown(pygame.sprite.Sprite):
    def __init__(self, bg_rect, screenObject):
        super(Unknown, self).__init__()
        self.bg_rect = bg_rect
        self.screenObject = screenObject
        self.moveLeft = [pygame.image.load('Images/game/unknown_left_1.png'),
                         pygame.image.load('Images/game/unknown_left_2.png')]
        self.unknown_standing = pygame.image.load('Images/game/unknown_0.png')
        self.moveRight = [pygame.image.load('Images/game/unknown_right_1.png'),
                          pygame.image.load('Images/game/unknown_right_2.png')]
        self.rect = self.unknown_standing.get_rect()
        self.rect.centerx = self.bg_rect.centerx
        self.rect.bottom = self.bg_rect.bottom - 15
        self.speed = 6
        self.animCnt = 0
        self.right = False
        self.left = False

    def place_unknown(self):
        if self.animCnt >= 29:
            self.animCnt = 0
        if self.left:
            self.screenObject.screen.blit(self.moveLeft[self.animCnt//15], self.rect)
        elif self.right:
            self.screenObject.screen.blit(self.moveRight[self.animCnt//15], self.rect)
        else:
            self.screenObject.screen.blit(self.unknown_standing, self.rect)
    def move_unknown(self):
        if self.right and self.rect.right <= self.bg_rect.right - 25:
            self.rect.centerx += self.speed
            self.animCnt += 1
        elif self.left and self.rect.left > self.bg_rect.left + 25:
            self.rect.centerx -= self.speed
            self.animCnt += 1