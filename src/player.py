import pygame

class Player:

    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

        self.dx = 0
        self.dy = 0

    def handle_keydown(self, key):
        if key == pygame.K_w:
            self.dy = -self.speed
        elif key == pygame.K_s:
            self.dy = self.speed
        elif key == pygame.K_a:
            self.dx = -self.speed
        elif key == pygame.K_d:
            self.dx = self.speed

    def handle_keyup(self, key):
        if key in (pygame.K_w, pygame.K_s):
            self.dy = 0
        elif key in (pygame.K_a, pygame.K_d):
            self.dx = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
