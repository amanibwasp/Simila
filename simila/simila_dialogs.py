import pygame
from common_settings.game import Game


class Simila_dialogs():
    def __init__(self, screenObject, simila, using_win):
        self.using_win = using_win
        self.screenObject = screenObject
        self.game = Game(self.screenObject)
        self.simila = simila

        self.run_dialog = False
        self.dialog_state = None
        self.option = ''

        self.first_meeting_image = pygame.image.load('Images\simila_dialogs\\first_meeting.png')
        self.first_meeting_1_image = pygame.image.load('Images\simila_dialogs\\first_meeting_1.png')
        self.first_meeting_2_image = pygame.image.load('Images\simila_dialogs\\first_meeting_2.png')
        self.first_meeting_3_image = pygame.image.load('Images\simila_dialogs\\first_meeting_3.png')
        self.first_meeting_4_image = pygame.image.load('Images\simila_dialogs\\first_meeting_4.png')
        self.answers_image = pygame.image.load('Images\simila_dialogs\\answers.png')

        # rect для всех диалогов
        self.dialog_rect = self.first_meeting_image.get_rect()
        self.dialog_rect.centerx = self.screenObject.screen_rect.centerx
        self.dialog_rect.bottom = self.screenObject.screen_rect.bottom

        self.dialog_rect_1 = pygame.Rect(self.dialog_rect.x, self.dialog_rect.y, self.dialog_rect.w // 2,
                                         self.dialog_rect.h // 2)
        self.dialog_rect_2 = pygame.Rect(self.dialog_rect.centerx, self.dialog_rect.y, self.dialog_rect.w // 2,
                                         self.dialog_rect.h // 2)
        self.dialog_rect_3 = pygame.Rect(self.dialog_rect.x, self.dialog_rect.centery, self.dialog_rect.w // 2,
                                         self.dialog_rect.h // 2)
        self.dialog_rect_4 = pygame.Rect(self.dialog_rect.centerx, self.dialog_rect.centery, self.dialog_rect.w // 2,
                                         self.dialog_rect.h // 2)

    def run_simila_dialog(self):
        match self.dialog_state + self.option:
            case None:
                self.screenObject.screen.blit(self.answers_image, self.dialog_rect)
            case 'first_meeting':
                self.screenObject.screen.blit(self.first_meeting_image, self.dialog_rect)
            case 'first_meeting_1':
                self.screenObject.screen.blit(self.first_meeting_1_image, self.dialog_rect)
            case 'first_meeting_2':
                self.screenObject.screen.blit(self.first_meeting_2_image, self.dialog_rect)
            case 'first_meeting_3':
                self.screenObject.screen.blit(self.first_meeting_3_image, self.dialog_rect)
            case 'first_meeting_4':
                self.screenObject.screen.blit(self.first_meeting_4_image, self.dialog_rect)

    def check_mouse_pos_for_options(self):
        if self.dialog_state != None:
            self.mouse_pos = pygame.mouse.get_pos()
            if self.dialog_rect_1.left <= self.mouse_pos[0] <= self.dialog_rect_1.right and self.dialog_rect_1.top <= \
                    self.mouse_pos[1] <= self.dialog_rect_1.bottom:
                self.option = '_1'
            elif self.dialog_rect_2.left <= self.mouse_pos[0] <= self.dialog_rect_2.right and self.dialog_rect_2.top <= \
                    self.mouse_pos[1] <= self.dialog_rect_2.bottom:
                self.option = '_2'
            elif self.dialog_rect_3.left <= self.mouse_pos[0] <= self.dialog_rect_3.right and self.dialog_rect_3.top <= \
                    self.mouse_pos[1] <= self.dialog_rect_3.bottom:
                self.option = '_3'
            elif self.dialog_rect_4.left <= self.mouse_pos[0] <= self.dialog_rect_4.right and self.dialog_rect_4.top <= \
                    self.mouse_pos[1] <= self.dialog_rect_4.bottom:
                self.option = '_4'
            else:
                self.option = ''

    def if_clicked(self):
        self.click = pygame.mouse.get_pressed()
        if self.click[0]:
            match self.dialog_state:
                case 'first_meeting':
                    match self.option:
                        case '_1':
                            self.simila.state = 'creepy'
                        case '_2':
                            self.game.run_game()
                            self.using_win.general_room_pk_close_running = False
                        case '_3':
                            self.simila.state = 'worried'
                        case '_4':
                            self.simila.state = 'disgust'
                        case '':
                            self.simila.state = 'happy'
