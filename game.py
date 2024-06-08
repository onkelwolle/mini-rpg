import sys
import time

class Game:
    def __init__(self):
        self.running = True
        self.map = self.load_map("map.txt")
    
    def load_map(self, filename):
        with open(filename, 'r') as file:
            return [list(line.strip()) for line in file]

    def run(self):
        while self.running:
            self.clear_screen()
            self.render()
            self.handle_input()
            self.update()

    def clear_screen(self):
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()

    def handle_input(self):
        command = input("Enter command: (w/a/s/d/talk/quit): ")
        if command in ['w', 'a', 's', 'd']:
            print("not implemented yet")
        elif command == 'talk':
            print("not implemented yet")
        elif command == 'quit':
            self.running = False

    def update(self):
        pass

    def render(self):
        for row in self.map:
            print(''.join(row))
