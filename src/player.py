import pygame

class Player:

    def __init__(self, x, y):
        self.width = 32
        self.height = 32

        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("blue")
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

    def update(self, map):
        new_x = self.rect.x + self.dx
        new_y = self.rect.y + self.dy

        new_rect = pygame.Rect(new_x, new_y, self.width, self.height)

        if(map.is_passable(new_rect)):
            self.rect = new_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
