import os
import random
import time
import keyboard
import pyfiglet
from rich.console import Console

from config import *
from render import *
from logger import *

os.system("")
console = Console()

def print_ascii(text):
    ascii_text = pyfiglet.figlet_format(text, font="big")
    print(ascii_text)

snake_positions = []
snake_length = 1

food_positions = []
food_list = []
food_time = time.time()

class Snake:
    def __init__(self):
        self.direction = 0
        self.x = 3
        self.y = int(GRID_SIZE/2)

        self.nx, self.ny = 0, 0

    def get_next_position(self):
        dx, dy = 0, 0
        if self.direction == 0:
            dx = 1
        elif self.direction == 1:
            dy = -1
        elif self.direction == 2:
            dx = -1
        elif self.direction == 3:
            dy = 1
        self.nx = self.x + dx
        self.ny = self.y + dy


    def check_collision(self):
        # Bounds collision
        if self.nx < 0 or self.nx >= GRID_SIZE:
            return True
        if self.ny < 0 or self.ny >= GRID_SIZE:
            return True

        # Self collision
        if (self.nx, self.ny) in snake_positions:
            return  True

        return False

    def move(self):
        self.get_next_position()
        if self.check_collision():
            return False
        else:
            self.x = self.nx
            self.y = self.ny
            return True

    def update(self):
        if keyboard.is_pressed("d"):
            if self.direction != 2:
                self.direction = 0
        if keyboard.is_pressed("w"):
            if self.direction != 3:
                self.direction = 1
        if keyboard.is_pressed("a"):
            if self.direction != 0:
                self.direction = 2
        if keyboard.is_pressed("s"):
            if self.direction != 1:
                self.direction = 3
        if not self.move():
            return False
        snake_positions.append((self.x, self.y))
        return True

class Food:
    def __init__(self):
        self.x = random.randint(0, GRID_SIZE)
        self.y = random.randint(0, GRID_SIZE)
        while (self.x, self.y) in snake_positions:
            self.x = random.randint(0, GRID_SIZE)
            self.y = random.randint(0, GRID_SIZE)
        food_positions.append((self.x, self.y))

snake = Snake()

log("info", "Game Started")
run = True
while run:
    if not snake.update():
        log("info", "Game over")
        run = False
        continue

    if len(snake_positions) > snake_length:
        snake_positions.pop(0)

    if ( time.time() - food_time ) > FOOD_INTERVAL:
        food_list.append(Food())
        food_time = time.time()

    grid_lines = draw_grid(GRID_SIZE, snake_positions[-snake_length:], food_positions)

    for i in range(len(grid_lines)):
        console.print(grid_lines[i])
    if run:
        move_cursor_up(GRID_SIZE)

    if keyboard.is_pressed("q"):
        log("info", "Game quit")
        run = False

    time.sleep(REFRESH_RATE)

for i in range(GRID_SIZE):
    print("")
print_ascii("Game Over!")