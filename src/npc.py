import pygame

class Npc:

    def __init__(self, x, y):
        self.width = 32
        self.height = 32
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
