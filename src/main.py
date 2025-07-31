import os
import time
import keyboard
from rich.console import Console

from config import *
from render import *

os.system("")
console = Console()

snake_positions = []
snake_length = 1

class Snake:
    def __init__(self):
        self.direction = 0
        self.x = 3
        self.y = int(GRID_SIZE/2)

    def move(self):
        # Future Collision Checks
        if self.direction == 0: # right
            self.x += 1
        elif self.direction == 1: # up
            self.y -= 1
        elif self.direction == 2: # left
            self.x -= 1
        elif self.direction == 3: # down
            self.y += 1
        else:
            return


    def update(self):
        if keyboard.is_pressed("d"):
            self.direction = 0
        if keyboard.is_pressed("w"):
            self.direction = 1
        if keyboard.is_pressed("a"):
            self.direction = 2
        if keyboard.is_pressed("s"):
            self.direction = 3
        self.move()
        snake_positions.append((self.x, self.y))

snake = Snake()

run = True
while run:
    snake.update()

    grid_lines = draw_grid(GRID_SIZE, snake_positions[-snake_length:])

    if len(snake_positions) > snake_length:
        snake_positions.pop()

    for i in range(len(grid_lines)):
        console.print(grid_lines[i])
    move_cursor_up(GRID_SIZE)

    if keyboard.is_pressed("q"):
        run = False


    time.sleep(REFRESH_RATE)