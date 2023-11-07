import pygame


class Simila():
    def __init__(self, screenObject):
        self.screenObject = screenObject
        self.simila_creepy = pygame.image.load('Images/simila/simila_creepy.png')
        self.simila_disgust = pygame.image.load('Images/simila/simila_disgust.png')
        self.simila_happy = pygame.image.load('Images/simila/simila_happy.png')
        self.simila_neutral = pygame.image.load('Images/simila/simila_neutral.png')
        self.simila_pleased = pygame.image.load('Images/simila/simila_pleased.png')
        self.simila_worried = pygame.image.load('Images/simila/simila_worried.png')
        self.simila_rect = self.simila_happy.get_rect()
        self.state = None

    def output_simila(self):
        match self.state:
            case 'happy':
                self.screenObject.screen.blit(self.simila_happy, self.simila_rect)
            case 'creepy':
                self.screenObject.screen.blit(self.simila_creepy, self.simila_rect)
            case 'disgust':
                self.screenObject.screen.blit(self.simila_disgust, self.simila_rect)
            case 'neutral':
                self.screenObject.screen.blit(self.simila_neutral, self.simila_rect)
            case 'pleased':
                self.screenObject.screen.blit(self.simila_pleased, self.simila_rect)
            case 'worried':
                self.screenObject.screen.blit(self.simila_worried, self.simila_rect)
