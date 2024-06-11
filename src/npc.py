import pygame
from ui import Ui

class Npc:

    def __init__(self, x, y):
        self.width = 32
        self.height = 32
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.chat_ui = Ui(10, 10, "The princess is in another castle")

    def update(self):
        pass

    def draw(self, player, screen):
        if self.rect.colliderect(player.rect):
            self.chat_ui.draw(screen)
        screen.blit(self.image, self.rect.topleft)
