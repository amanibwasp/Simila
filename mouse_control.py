import pygame
class Mouse_control():

    def pos_and_click_for_dialog(self, dialog, action):
        self.action = action
        self.dialog = dialog
        self.rect = self.dialog.rect
        self.click = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        if self.rect.left <= self.mouse_pos[0] <= self.rect.right and self.rect.top <= self.mouse_pos[1] <= self.rect.bottom:
            if self.click[0]:
                pygame.time.delay(300)
                match self.dialog.dialog_phase:
                    case 'where':
                        self.dialog.dialog_phase = 'observe'
                    case 'observe':
                        self.action()
                    case 'general_room_greetings':
                        self.action()




