import pygame
import random
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_SIZE, POWERUP_TYPES

# Preload power-up images for performance
powerup_images = {}
for ptype in POWERUP_TYPES:
    try:
        # Ensure these images exist in the assets/powerups folder
        image = pygame.image.load(f'assets/powerups/{ptype}.png')
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        powerup_images[ptype] = image
    except FileNotFoundError:
        print(f"Error: 'assets/powerups/{ptype}.png' not found.")
        # Create a placeholder surface if image not found
        placeholder = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        placeholder.fill((255, 0, 255))  # Magenta as placeholder
        powerup_images[ptype] = placeholder

class PowerUp:
    def __init__(self):
        # Randomly choose a power-up type
        self.type = random.choice(POWERUP_TYPES)
        self.x = random.randint(0, SCREEN_WIDTH - SQUARE_SIZE)
        self.y = -SQUARE_SIZE
        self.image = powerup_images[self.type]

    def move(self, fall_speed):
        self.y += fall_speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def has_collided_with_player(self, player):
        powerup_rect = pygame.Rect(self.x, self.y, SQUARE_SIZE, SQUARE_SIZE)
        return powerup_rect.colliderect(player.rect)
