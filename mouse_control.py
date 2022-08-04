import pygame
class Mouse_control():

    def pos_and_click_for_dialog(self, dialog = None, action = None, simila_dialogs = None):
        self.simila_dialogs = simila_dialogs
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
                    case 'simila_greetings':
                        self.dialog.dialog_phase = 'game_offer'
                    case 'game_offer':
                        self.simila_dialogs.dialog_state = 'first_meeting'
                        self.simila_dialogs.run_dialog = True
                        self.dialog.dialog_phase = None





