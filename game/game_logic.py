import pygame
import random
from game.constants import *
from game.game_state import GameState
from game.player import Player
from game.square import Square
from game.power_up import PowerUp
from services.game_over_services import GameOverService

class Game:
    def __init__(self, screen, clock, username, score_font, item_fall_speed, spawn_rate, max_misses):
        self.screen = screen
        self.clock = clock
        self.username = username
        self.player = Player(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2,
                             SCREEN_HEIGHT - PLAYER_HEIGHT - 10,
                             'assets/player/player.png')
        self.squares = []
        self.powerups = []
        self.collision_counter = 0
        self.spawn_counter = 0
        self.item_fall_speed = item_fall_speed
        self.spawn_rate = spawn_rate
        self.game_over_services = GameOverService(max_misses, username)
        self.heart_image = self.load_heart_image()
        self.sounds = self.load_sounds()
        self.game_over_sound_played = False
        self.score_font = score_font
        self.powerup_timer = 0
        
        # Combo system: counts how many objects caught consecutively
        self.combo_count = 0

        # Background
        try:
            self.background_image = pygame.image.load('assets/BG.jpg')
            self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.background_image = None

    def load_heart_image(self):
        try:
            heart_image = pygame.image.load('assets/heart.png')
            return pygame.transform.scale(heart_image, (30, 30))
        except Exception as e:
            print(f"Error loading heart image: {e}")
            return None

    def load_sounds(self):
        sounds = {}
        try:
            sounds['catch'] = pygame.mixer.Sound('assets/sounds/catch_object.wav')
            sounds['miss'] = pygame.mixer.Sound('assets/sounds/missed_object.wav')
            sounds['game_over'] = pygame.mixer.Sound('assets/sounds/game_over_sound.wav')
            sounds['background'] = pygame.mixer.Sound('assets/sounds/game_background.wav')
            sounds['extra_life'] = pygame.mixer.Sound('assets/sounds/extra_life.wav')
            sounds['slow_motion'] = pygame.mixer.Sound('assets/sounds/slow_motion.wav')
            sounds['multiplier'] = pygame.mixer.Sound('assets/sounds/score_multiplier.wav')
            sounds['bomb'] = pygame.mixer.Sound('assets/sounds/bomb.wav')  # Add a bomb sound

            # Adjust volumes
            for sound_name in sounds:
                sounds[sound_name].set_volume(0.8)
            sounds['background'].set_volume(0.2)

            # Play background music
            pygame.mixer.music.load('assets/sounds/game_background.wav')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1, 0.0)
        except Exception as e:
            print(f"Error loading sound: {e}")
            return {}
        return sounds

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def spawn_square(self):
        self.squares.append(Square())

    def spawn_powerup(self):
        self.powerup_timer += 1
        if self.powerup_timer >= POWERUP_INTERVAL or random.randint(1, 100) <= POWERUP_SPAWN_CHANCE:
            new_powerup = PowerUp()
            powerup_rect = pygame.Rect(new_powerup.x, new_powerup.y, SQUARE_SIZE, SQUARE_SIZE)
            for square in self.squares:
                if powerup_rect.colliderect(square.get_rect()):
                    return
            self.powerups.append(new_powerup)
            self.powerup_timer = 0

    def draw_game_state(self):
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        else:
            self.screen.fill(WHITE)  # Fallback background

        # Draw lives as hearts
        if self.heart_image:
            for i in range(self.game_over_services.max_misses - self.game_over_services.missed_count):
                self.screen.blit(self.heart_image, (SCREEN_WIDTH - (i + 1) * 50, 10))

        if not self.game_over_services.game_over:
            # Show score and combo
            combo_display = f"Combo: {self.combo_count}"
            score_text = self.score_font.render(f"Score: {self.collision_counter}", True, BLACK)
            combo_text = self.score_font.render(combo_display, True, BLACK)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(combo_text, (10, 40))

        self.player.draw(self.screen)
        for square in self.squares:
            square.draw(self.screen)
        for powerup in self.powerups:
            powerup.draw(self.screen)

    def update_game_state(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        self.spawn_counter += 1
        if self.spawn_counter >= self.spawn_rate * FPS:
            self.spawn_square()
            self.spawn_powerup()
            self.spawn_counter = 0

        # Update squares
        for square in self.squares[:]:
            square.move(self.item_fall_speed)
            if square.is_off_screen():
                self.squares.remove(square)
                missed = self.game_over_services.check_object_missed(
                    pygame.Rect(square.x, square.y, SQUARE_SIZE, SQUARE_SIZE), SCREEN_HEIGHT)
                if missed and not self.game_over_services.game_over:
                    self.play_sound('miss')
                    # Reset combo on miss
                    self.combo_count = 0
            elif square.has_collided_with_player(self.player.rect):
                self.squares.remove(square)
                self.play_sound('catch')
                # Increase combo and score
                self.combo_count += 1
                # Example scoring: base 1 point + bonus for every 5 catches in combo
                bonus = (self.combo_count // COMBO_THRESHOLD)
                self.collision_counter += (COMBO_SCORE_INCREMENT + bonus)

        # Update powerups
        for powerup in self.powerups[:]:
            powerup.move(self.item_fall_speed)
            if powerup.is_off_screen():
                self.powerups.remove(powerup)
            elif powerup.has_collided_with_player(self.player):
                # Handle each power-up type
                if powerup.type == 'extralife':
                    self.game_over_services.add_life()
                    self.play_sound('extra_life')
                elif powerup.type == 'slowmotion':
                    self.item_fall_speed = max(self.item_fall_speed // 2, 1)
                    self.play_sound('slow_motion')
                elif powerup.type == 'multiplier':
                    self.collision_counter += 10
                    self.play_sound('multiplier')
                elif powerup.type == 'bomb':
                    # Bomb reduces life
                    self.game_over_services.register_missed_object()
                    self.play_sound('bomb')
                    # Reset combo when bomb is caught
                    self.combo_count = 0

                self.powerups.remove(powerup)

        # Check game over
        if self.game_over_services.is_game_over():
            if not self.game_over_sound_played:
                self.play_sound('game_over')
                self.game_over_sound_played = True
            self.squares.clear()
            self.powerups.clear()
            return GameState.GAME_OVER

        return GameState.GAME
