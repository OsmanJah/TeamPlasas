# Toy Catcher: A Whimsical Adventure

Toy Catcher is a Python-based arcade game where players attempt to catch falling toys before they hit the ground. With multiple difficulty levels, exciting power-ups, and vibrant visuals, the game provides a challenging yet entertaining experience.

## Features

### Multiple Difficulty Levels
- Easy, Medium, and Hard — each mode adjusts falling speed and maximum lives.

### Power-Ups and Surprises
- Extra Life: Gain an additional life
- Slow Motion: Temporarily reduce falling speed
- Multiplier: Instantly add a score bonus
- Bomb: Negative power-up that deducts a life if caught

### Combo Scoring System
- Consecutive catches without dropping a toy build a combo counter
- Reach certain thresholds to boost your score significantly

### Interactive Menus
- Main Menu: Start Game, Leaderboard, How to Play, Settings, Exit
- Settings: Toggle background music or sound effects on/off
- Leaderboard: View top scores and your personal high scores

### Visual & Audio Feedback
- Sound Effects: Distinct audio cues for catching toys, missing toys, and power-ups
- Background Music: Engaging soundtrack that can be paused/resumed in Settings
- Colorful Graphics: Bright, cheerful toy sprites, fun backgrounds, and a charming player character

### High Score Persistence
- Utilizes a local SQLite database to store and display top scores across sessions

## Technology Used
- Python 3.7+: Core language for game logic
- Pygame: Library for graphics, user input, and sound management
- SQLite: Database to store and retrieve high scores

## Setup Instructions

### Clone or Download the Project
```bash
git clone https://github.com/OsmanJah/TeamPlasas.git
```

### Install Prerequisites
Make sure Python 3.7+ is installed on your system, then install the required dependencies:

```bash
pip install pygame
```

### Run the Game
Navigate to your project directory and run:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

### Assets Required
Confirm that images (player, toy items, power-ups) and audio files (music, sound effects) are in the correct `assets/` folders. If you encounter missing-file errors, check `constants.py` and `power_up.py` for the exact paths.

## How to Play

### Launch the Game
Run `python main.py` to open the Main Menu.

### Enter a Username
Type your desired username and press Enter.

### Select a Difficulty
Choose Easy, Medium, or Hard. Each mode has different falling speeds and maximum life counts.

### Catch Toys
Use the movement keys (see Controls) to position your character and catch falling toys. Avoid letting too many toys slip past you; if you lose all your lives, the game ends.

### Utilize Power-Ups
- Extra Life, Slow Motion, and Multiplier to gain various advantages
- Bomb power-ups cause you to lose a life if caught

### Game Over
Occurs when you run out of lives. Your score is saved if it makes it onto the Leaderboard.

## Controls

- **Move Left**: Left Arrow Key or A
- **Move Right**: Right Arrow Key or D
- **Pause the Game**: Press P during gameplay
- **Settings**: Access via the Main Menu to toggle sound/music
- **Exit**: Use the Exit button on the Main Menu or close the game window directly

Enjoy Toy Catcher!
