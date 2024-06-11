import pygame

class Ui:
    
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text = self.font.render(self.text, True, "white")
        screen.blit(text, (self.x, self.y))
