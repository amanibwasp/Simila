import pygame
from screen import Screen
from startMenu import StartMenu

class Main():
    pygame.init()
    def __init__(self):
        screenObject = Screen()
        sm = StartMenu(screenObject)
mw = Main()






