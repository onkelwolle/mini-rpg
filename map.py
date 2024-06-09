import pygame

class Map:

    def __init__(self):
        self.map_data = [
            "############################",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "#                          #",
            "############################",
        ]

    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, char in enumerate(row):
                if char == "#":
                    pygame.draw.rect(screen, "gray", pygame.Rect(x*32, y*32, 32, 32))
