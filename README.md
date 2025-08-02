# 🐍 Terminal Snake Game

A classic **Snake** game made in Python that runs right in your terminal!  

## 🚀 Features

- Colourful grid with alternating grass tones.
- Snake head and body are visually distinct.
- ASCII-art game over message.
- Dynamic side text showing your score.
- Logging support for debugging and events.
- Clean code structure with separate files for config, rendering, and logging.

---

## 📦 Installation

Install the dependencies
``` bash
pip install -r requirements.txt
```
Run the game
``` bash
python main.py
```
> Use powershell or windows terminal for best color compatibility with color codes and rich.

---

## 🎮 How to play

- `W`: Move Up

- `A`: Move Left

- `S`: Move Down

- `D`: Move Right

- Eat apples (<span style='color: red;'>██</span>) to grow the snake.

- Don’t hit the walls or your own body.

- Press `Q` at any time to quit the game.

- The game gets faster as your score increases!

## 📁 File Structure

```
terminal-snake/
├── main.py              # Main game logic
├── config.py            # Game settings like grid size and food interval
├── render.py            # Grid rendering and side text generation
├── logger.py            # Logging system for game events
├── requirements.txt     # Required packages
└── README.md            # You're reading it!
```

---
