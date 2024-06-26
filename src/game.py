import pygame
from player import Player
from npc import Npc
from map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Map()
        self.player = Player(64, 64)
        self.npcs = [Npc(128, 128)]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.player.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.player.handle_keyup(event.key)

    def render(self):
        self.screen.fill("black")
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        for npc in self.npcs:
            npc.draw(self.player, self.screen)
        pygame.display.flip()

    def update(self):
        self.map.update(self.player, self.npcs)
        self.player.update(self.map)
        for npc in self.npcs:
            npc.update()
