import pygame
from common_settings.screen import Screen
from menu.startMenu import StartMenu

class Main():
    pygame.init()
    def __init__(self):
        screenObject = Screen()
        sm = StartMenu(screenObject)
mw = Main()






