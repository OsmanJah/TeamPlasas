import pygame
from services.main_menu import main_menu, show_leaderboard, pause_menu
from services.get_username import get_username
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.game_logic import Game
from game.game_state import GameState
from utils import Button  # Only import Button from utils
from game.constants import BLACK, WHITE, GREY  # Import colors from constants

def show_difficulty_menu(screen, clock):
    pygame.font.init()
    font = pygame.font.Font(None, 50)

    difficulties = ["Easy", "Medium", "Hard"]

    # Create buttons for each difficulty
    button_width = 200
    button_height = 50
    button_spacing = 20
    start_y = SCREEN_HEIGHT // 3

    difficulty_buttons = []
    for i, diff in enumerate(difficulties):
        btn = Button(
            diff,
            SCREEN_WIDTH // 2 - button_width // 2,
            start_y + i * (button_height + button_spacing),
            button_width,
            button_height,
            WHITE,
            GREY,
            font
        )
        difficulty_buttons.append(btn)

    running = True
    while running:
        # Change background to white
        screen.fill(WHITE)

        title = font.render("Select Difficulty", True, BLACK)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 4))

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        # Draw and handle clicks on difficulty buttons
        for btn in difficulty_buttons:
            btn.draw(screen, mouse_pos)
            if btn.is_clicked(mouse_pos, mouse_pressed):
                return btn.text  # Return the difficulty selected

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Optional: Add keyboard support if desired

        pygame.display.flip()
        clock.tick(FPS)

def main():
    pygame.init()
    score_font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Change game name:
    pygame.display.set_caption('Catching Toys')
    clock = pygame.time.Clock()

    username = get_username(screen, clock)

    state = GameState.MAIN_MENU
    game = None
    game_over = False
    sound_on = True  # Initial sound state

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and state == GameState.GAME:
                if event.key == pygame.K_p:  # Press 'P' to pause
                    state = GameState.PAUSE

        if state == GameState.MAIN_MENU:
            state, sound_on = main_menu(screen, clock, pygame.font.Font(None, 36), game_over, sound_on)

            if state == GameState.GAME:
                difficulty = show_difficulty_menu(screen, clock)
                if difficulty == "Easy":
                    item_fall_speed = 5
                    spawn_rate = 2
                    max_misses = 5
                elif difficulty == "Medium":
                    item_fall_speed = 8
                    spawn_rate = 1.5
                    max_misses = 3
                elif difficulty == "Hard":
                    item_fall_speed = 12
                    spawn_rate = 1
                    max_misses = 2

                # Initialize the game with selected difficulty
                game = Game(screen, clock, username, score_font, item_fall_speed, spawn_rate, max_misses)
                game_over = False

                # Control sound
                if not sound_on:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

        elif state == GameState.LEADERBOARD:
            show_leaderboard(screen, clock, pygame.font.Font(None, 36), username)
            state = GameState.MAIN_MENU

        elif state == GameState.GAME:
            state = game.update_game_state()
            game.draw_game_state()
            pygame.display.flip()
            clock.tick(FPS)

        elif state == GameState.GAME_OVER:
            game_over = True
            show_leaderboard(screen, clock, pygame.font.Font(None, 36), username)
            state = GameState.MAIN_MENU

        elif state == GameState.PAUSE:
            state = pause_menu(screen, clock, pygame.font.Font(None, 36))


if __name__ == '__main__':
    main()
