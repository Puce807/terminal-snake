import os
import random
import time
import keyboard
import pyfiglet
from rich.console import Console

from config import *
from render import *
from logger import *

console = Console()
os.system("")

def print_ascii(text):
    ascii_text = pyfiglet.figlet_format(text, font="big")
    print(ascii_text)

snake_positions = []
food_positions = []
food_list = []
food_count = 0
food_time = time.time()

score = 0

class Snake:
    def __init__(self):
        self.direction = 0
        self.x = 3
        self.y = int(GRID_SIZE/2)

        self.nx, self.ny = 0, 0

        self.length = 1

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
            return "hit"
        if self.ny < 0 or self.ny >= GRID_SIZE:
            return "hit"

        # Self collision
        if (self.nx, self.ny) in snake_positions:
            return  "hit"

        # Food collision
        if (self.nx, self.ny) in food_positions:
            return "Food"

        return False

    def move(self):
        self.get_next_position()
        result = self.check_collision()
        if result == "hit":
            return False
        elif result == "Food":
            self.length += 1
            self.x = self.nx
            self.y = self.ny
            return  True
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
        self.position = (self.x, self.y)
        while (self.x, self.y) in snake_positions:
            self.x = random.randint(0, GRID_SIZE)
            self.y = random.randint(0, GRID_SIZE)
        food_positions.append((self.x, self.y))
        self.dead = False

    def collision(self):
        log("info", f"Position: {self.position}")
        log("info", f"Snake positions: {snake_positions}")
        if self.position in snake_positions:
            if self.position in food_positions:
                food_positions.remove(self.position)
            food_list.remove(self)

            self.dead = True
            return True
        return False

snake = Snake()

side_text = [
    "--- Terminal Snake ---",
    "",
    ""
]


log("info", "Game Started")
os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
run = True
while run:
    if not snake.update():
        log("info", "Game over")
        run = False
        continue

    for food in food_list[:]:
        if food.collision():
            food_count -= 1
            score += 1

    if len(snake_positions) > snake.length:
        snake_positions.pop(0)

    if ( time.time() - food_time ) > FOOD_INTERVAL:
        if food_count < MAX_FOOD:
            food_list.append(Food())
            food_time = time.time()
            food_count += 1

    side_text[2] = f"Score: {score}"

    grid_lines = generate_grid(GRID_SIZE, snake_positions[-snake.length:], food_positions)
    grid_lines = generate_side_text(grid_lines, side_text)

    for text in grid_lines:
        console.print(text)

    move_cursor_up(GRID_SIZE)

    if keyboard.is_pressed("q"):
        log("info", "Game quit")
        run = False

    time.sleep(REFRESH_RATE)

for i in range(GRID_SIZE):
    print("")
print_ascii("Game Over!")