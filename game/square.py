import pygame
import random
from game.constants import SQUARE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Square:
    # Load and scale images once
    images = [
        pygame.transform.scale(
            pygame.image.load(f'assets/obj{i}.png'),
            (SQUARE_SIZE * 1.3, SQUARE_SIZE * 1.3)
        ) for i in range(1, 17)
    ]

    def __init__(self):
        self.image = random.choice(Square.images)
        self.x = random.randint(0, SCREEN_WIDTH - int(SQUARE_SIZE * 1.3))
        self.y = -int(SQUARE_SIZE * 1.3)

    def move(self, fall_speed):
        self.y += fall_speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def has_collided_with_player(self, player):
        square_rect = self.get_rect()
        return square_rect.colliderect(player)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, int(SQUARE_SIZE * 1.3), int(SQUARE_SIZE * 1.3))
