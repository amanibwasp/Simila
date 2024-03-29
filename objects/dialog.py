import pygame


class Dialog():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.image_dialog = pygame.image.load("Images/dialog templates/dialog.png")
        self.image_dialog_where = pygame.image.load("Images/dialog templates/where.png")
        self.image_dialog_observe = pygame.image.load("Images/dialog templates/observe.png")
        self.image_dialog_general_room_greetings = pygame.image.load(
            "Images/dialog templates/general_room_greetings.png")
        self.rect = self.image_dialog_where.get_rect()
        self.screen_rect = screenObject.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.dialog_phase = None

        # фразы Симилы:
        self.simila_greetings = pygame.image.load('Images/simila_dialogs/simila_greetings.png')
        self.game_offer = pygame.image.load('Images/simila_dialogs/game_offer.png')

    def place_dialog(self):
        self.screenObject.screen.blit(self.image_dialog, self.rect)

    def kill_dialog(self):
        self.dialog_phase = None

    def update_dialog(self):
        match self.dialog_phase:
            case 'where':
                self.screenObject.screen.blit(self.image_dialog_where, self.rect)
            case 'observe':
                self.screenObject.screen.blit(self.image_dialog_observe, self.rect)
            case 'general_room_greetings':
                self.screenObject.screen.blit(self.image_dialog_general_room_greetings, self.rect)
            case 'simila_greetings':
                self.screenObject.screen.blit(self.simila_greetings, self.rect)
            case 'game_offer':
                self.screenObject.screen.blit(self.game_offer, self.rect)
