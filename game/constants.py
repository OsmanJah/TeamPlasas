GREY = (200, 200, 200)
DARK_GREY = (50, 50, 50)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
MOVE_SPEED = 10
SQUARE_SIZE = 30
SPAWN_RATE = 100
FALL_SPEED = 3
FPS = 60
MAX_MISSES = 3
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LEVEL_1_THRESHOLD = 20
LEVEL_2_THRESHOLD = 40
LEVEL_SPEEDS = {
    1: 3,  # Base speed for level 1
    2: 6,  # Increased speed for level 2
    3: 9   # Maximum speed for level 3
}

POWERUP_INTERVAL = 300        # Frames after which we try to spawn a power-up
POWERUP_SPAWN_CHANCE = 20     # Percentage chance to spawn a power-up each spawn cycle

# Added a negative "bomb" as a power-up type
POWERUP_TYPES = ['extralife', 'slowmotion', 'multiplier', 'bomb']

# Combo scoring (optional adjustments)
COMBO_SCORE_INCREMENT = 1  # Base score per catch
COMBO_THRESHOLD = 5        # Increase bonus every 5 consecutive catches
