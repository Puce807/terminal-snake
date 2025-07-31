
def move_cursor_up(lines=1):
    print(f"\033[{lines}A", end='')

def draw_grid(grid_size):
    grid_lines = []
    for y in range(grid_size):
        line = ""
        add = y % 2
        for x in range(grid_size):
            color = 0 if x % 2 == 0 else 1
            color = (color + add) % 2
            if color == 0:
                line += "[#AAD751]██[/#AAD751]"
            elif color == 1:
                line += "[#1CA64E]██[/#1CA64E]"
        grid_lines.append(line)
    return grid_lines

