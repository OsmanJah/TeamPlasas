Toy Catcher: A Whimsical Adventure
Toy Catcher is a Python-based arcade game where players attempt to catch falling toys before they hit the ground. With multiple difficulty levels, exciting power-ups, and vibrant visuals, the game provides a challenging yet entertaining experience.

Table of Contents
Features
Technology Used
Setup Instructions
How to Play
Controls
Features <a name="features"></a>
Multiple Difficulty Levels
Choose among Easy, Medium, or Hard, each with progressively faster falling speeds and varied maximum life counts.

Power-Ups and Surprises

Extra Life: Increases your remaining lives by one.
Slow Motion: Temporarily halves the falling speed of toys.
Multiplier: Instantly adds a score bonus.
Bomb: A negative power-up that causes you to lose a life if caught, raising the stakes.
Combo Scoring System
Consecutive catches without dropping any toy increase a combo counter, boosting your score whenever you reach certain thresholds.

Interactive Menus

Main Menu: Start Game, Leaderboard, How to Play, Settings, Exit.
Settings: Toggle background music or sound effects on/off.
Leaderboard: View top scores and your personal high scores.
Visual & Audio Feedback

Sound Effects: Distinct audio cues for catching toys, missing toys, and power-ups.
Background Music: Engaging background track that can be paused/resumed in Settings.
High-Quality Graphics: Colorful toy sprites, fun backgrounds, and a charming player character.
High Score Persistence
Utilizes a local SQLite database to store and display top scores.

Technology Used <a name="technology-used"></a>
Python 3.7+: The core language for game logic and flow control.
Pygame: A library providing graphics rendering, input handling, and sound management.
SQLite: Stores high scores and makes them persist across sessions.
Setup Instructions <a name="setup-instructions"></a>
Clone or Download the Project

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Install Prerequisites

Ensure Python 3.7+ is installed.
Install dependencies using pip:
bash
Copy code
pip install pygame
Run the Game

In the project directory, run:
bash
Copy code
python main.py
(Some systems may require python3 main.py.)
Assets Required

Make sure images (player, toy items, power-ups) and audio files (music, sound effects) are in the correct assets/ directories.
Check constants.py and power_up.py for file paths if you encounter missing file errors.
How to Play <a name="how-to-play"></a>
Launch the game to reach the Main Menu.
Enter a Username: Type your desired username and press Enter.
Select a Difficulty: Choose Easy, Medium, or Hard — each offers unique speed settings and life limits.
Catch Toys: Move your player left and right to collect falling toys.
Avoid letting too many toys slip past you; losing all your lives ends the game.
Utilize Power-Ups:
Extra Life for an additional life.
Slow Motion to temporarily slow falling speeds.
Multiplier to instantly boost your score.
Bomb power-ups reduce your life if caught, so watch out!
Game Over:
Happens when you run out of lives.
Your score is saved to the Leaderboard if it’s among the top scores.
Controls <a name="controls"></a>
Movement:
Left Arrow or A to move left.
Right Arrow or D to move right.
Pause: Press P during gameplay to pause the action.
Settings: Access via the Main Menu to toggle sound/music.
Exit: Use the Exit button on the main menu or close the game window directly.
Enjoy Toy Catcher, and feel free to contribute or report any issues to help improve the game!