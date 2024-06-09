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

    def is_passable(self, x, y):
        grid_x = x // 32
        grid_y = y // 32

        if 0 <= grid_y < len(self.map_data) and 0 <= grid_x < len(self.map_data[0]):
            return self.map_data[grid_y][grid_x] != "#"
        return False
