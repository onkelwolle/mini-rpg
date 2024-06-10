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

    def update(self, player, npcs):
        map_rows = [list(row) for row in self.map_data]
        
        for y in range(len(map_rows)):
            for x in range(len(map_rows[y])):
                if map_rows[y][x] in ("P", "N"):
                    map_rows[y][x] = " "

        player_x = player.rect.x // 32
        player_y = player.rect.y // 32
        if 0 <= player_y <= len(map_rows) and 0 <= player_x <= len(map_rows[player_y]): 
            map_rows[player_y][player_x] = "P"

        for npc in npcs:
            npc_x = npc.rect.x // 32
            npc_y = npc.rect.y // 32
            if 0 <= npc_y <= len(map_rows) and 0 <= npc_x <= len(map_rows[npc_y]):
                map_rows[npc_y][npc_x] = "N"

        self.map_data = ["".join(row) for row in map_rows]

    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, char in enumerate(row):
                if char == "#":
                    pygame.draw.rect(screen, "gray", pygame.Rect(x*32, y*32, 32, 32))

    def is_passable(self, rect):
        corners = [
                (rect.left, rect.top),
                (rect.right, rect.top),
                (rect.left, rect.bottom),
                (rect.right, rect.bottom)
        ]

        for (x, y) in corners:
            grid_x = x // 32
            grid_y = y // 32

            if 0 <= grid_y < len(self.map_data) and 0 <= grid_x < len(self.map_data[0]):
                if self.map_data[grid_y][grid_x] == "#":
                    return False
                elif self.map_data[grid_y][grid_x] == "N":
                    return False

        return True
