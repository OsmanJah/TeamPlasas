import pygame
import sys
from services.leaderboard_service import LeaderboardService

class GameOverService:
    def __init__(self, max_misses=3, username: str = "Player"):
        self.max_misses = max_misses
        self.missed_count = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.white_color = (255, 255, 255)
        self.leaderboard_service = LeaderboardService()
        self.username = username
        self.player_score = 0
        self.score_saved = False

    def register_missed_object(self):
        if not self.game_over:
            self.missed_count += 1
            if self.missed_count >= self.max_misses:
                self.end_game(self.player_score)

    def add_life(self):
        if self.missed_count > 0:
            self.missed_count -= 1
            print(f"Extra Life! Missed Count: {self.missed_count}")

    def end_game(self, final_score):
        self.game_over = True
        self.player_score = final_score
        print(f"Saving score: {self.username} - {self.player_score}")
        try:
            self.leaderboard_service.save_score(self.username, self.player_score)
            self.score_saved = True
            print("Score saved successfully.")
        except Exception as e:
            print(f"Error saving score: {e}")

    def reset_game(self):
        self.missed_count = 0
        self.game_over = False
        self.player_score = 0
        self.score_saved = False

    def is_game_over(self):
        return self.game_over

    def check_object_missed(self, object_rect, screen_height):
        if object_rect.top > screen_height:
            self.register_missed_object()
            return True
        return False
