from rich.text import Text

def move_cursor_up(lines=1):
    print(f"\033[{lines}A", end='')

def generate_grid(grid_size, snake_positions, food_positions):
    grid_lines = []
    for y in range(grid_size):
        line = ""
        add = y % 2
        for x in range(grid_size):
            color = 0 if x % 2 == 0 else 1
            color = (color + add) % 2
            for idx, (sx, sy) in enumerate(snake_positions):
                if sx == x and sy == y:
                    color = 2 if idx == len(snake_positions)-1 else 3
                    break
            for pos in food_positions:
                if pos == (x, y):
                    color = 4

            if color == 0: # Background lighter
                line += "[#AAD751]██[/#AAD751]" # [#AAD751]██[/#AAD751]
            elif color == 1: # Background darker
                line += "[#1CA64E]██[/#1CA64E]" # "[#1CA64E]██[/#1CA64E]"
            elif color == 2: # Snake Head
                line += "[#507EF5]██[/#507EF5]"
            elif color == 3: # Snake Body
                line += "[#426FE3]██[/#426FE3]"
            elif color == 4: # Food
                line += "[red]██[/red]"
        grid_lines.append(line)
    return grid_lines

def generate_side_text(grid_lines, side_text):
    lines = []
    for idx, line in enumerate(grid_lines):
        # Convert line and side text to Text objects
        rich_line = Text.from_markup(line)
        if len(side_text) > idx:
            rich_line.append(" " + side_text[idx])
        lines.append(rich_line)
    return lines
