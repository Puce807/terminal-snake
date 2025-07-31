import os
from rich.console import Console

from config import *
from render import *

os.system("")
console = Console()

grid_lines = draw_grid(GRID_SIZE)
for i in range(len(grid_lines)):
    console.print(grid_lines[i])

