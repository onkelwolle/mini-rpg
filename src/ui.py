import pygame

class Ui:
    
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text = self.font.render("Mini RPG", True, "white")
        screen.blit(text, (10, 10))
