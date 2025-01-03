import pygame
from services.leaderboard_service import LeaderboardService
from game.constants import *
from utils import Button
import sys
from game.game_state import GameState
from game.constants import BLACK, WHITE, GREY  # Import colors from constants

def main_menu(screen, clock, font, game_over=False, sound_on=True):
    button_width = 250
    button_height = 50
    button_spacing = 20
    start_y = SCREEN_HEIGHT // 2 - (button_height + button_spacing) * 2

    # Load the background image
    try:
        background_image = pygame.image.load('assets/BG.jpg')
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except Exception as e:
        print(f"Error loading background image: {e}")
        background_image = None

    main_button_text = "Restart" if game_over else "Start Game"
    main_button = Button(
        main_button_text,
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y,
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    leaderboard_button = Button(
        "Leaderboard",
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y + button_height + button_spacing,
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    how_to_play_button = Button(
        "How to Play",
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y + 2 * (button_height + button_spacing),
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    settings_button = Button(
        "Settings",
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y + 3 * (button_height + button_spacing),
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    exit_button = Button(
        "Exit",
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y + 4 * (button_height + button_spacing),
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    buttons = [main_button, leaderboard_button, how_to_play_button, settings_button, exit_button]

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BLACK)

        for button in buttons:
            button.draw(screen, mouse_pos)
            if button.is_clicked(mouse_pos, mouse_pressed):
                if button.text in ["Start Game", "Restart"]:
                    return GameState.GAME, sound_on
                elif button.text == "Leaderboard":
                    return GameState.LEADERBOARD, sound_on
                elif button.text == "How to Play":
                    show_instructions(screen, font)
                elif button.text == "Settings":
                    sound_on = show_settings(screen, font, sound_on, clock)
                elif button.text == "Exit":
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

def show_instructions(screen, font):
    running = True
    back_button = Button(
        "Back",
        SCREEN_WIDTH // 2 - 50,
        SCREEN_HEIGHT - 100,
        100,
        50,
        WHITE,
        GREY,
        font
    )

    instructions = [
        "How to Play:",
        "Use LEFT/RIGHT arrows or A/D to move.",
        "Catch falling toys to score points.",
        "Don't let them fall off screen or you lose a life!",
        "Power-Ups:",
        " - Extra Life: Gives you an extra life.",
        " - Slow Motion: Halves the fall speed.",
        " - Multiplier: Adds +10 to your score.",
        " - Bomb: Lose a life if caught!",
        "Combo System:",
        " - Each consecutive catch increases combo.",
        " - Every 5 consecutive catches increases bonus score!"
    ]

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        y_offset = 50
        for line in instructions:
            line_surf = font.render(line, True, BLACK)
            screen.blit(line_surf, (SCREEN_WIDTH // 2 - line_surf.get_width() // 2, y_offset))
            y_offset += 40

        back_button.draw(screen, mouse_pos)
        if back_button.is_clicked(mouse_pos, mouse_pressed):
            running = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

def show_settings(screen, font, sound_on, clock):
    running = True
    button_width = 200
    button_height = 50

    toggle_sound_button = Button(
        f"Sound: {'On' if sound_on else 'Off'}",
        SCREEN_WIDTH // 2 - button_width // 2,
        SCREEN_HEIGHT // 2 - button_height,
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    back_button = Button(
        "Back",
        SCREEN_WIDTH // 2 - 50,
        SCREEN_HEIGHT // 2 + 60,
        100,
        50,
        WHITE,
        GREY,
        font
    )

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        title_surf = font.render("Settings", True, BLACK)
        screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, SCREEN_HEIGHT // 4))

        toggle_sound_button.draw(screen, mouse_pos)
        if toggle_sound_button.is_clicked(mouse_pos, mouse_pressed):
            sound_on = not sound_on
            toggle_sound_button.text = f"Sound: {'On' if sound_on else 'Off'}"
            if sound_on:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()

        back_button.draw(screen, mouse_pos)
        if back_button.is_clicked(mouse_pos, mouse_pressed):
            # Return immediately after one click
            return sound_on

        pygame.display.flip()
        clock.tick(FPS)

def show_leaderboard(screen, clock, font, username):
    back_button = Button(
        "Back to Menu",
        50,
        SCREEN_HEIGHT - 100,
        150,
        50,
        WHITE,
        GREY,
        font
    )

    leaderboard_service = LeaderboardService()
    top_scores = leaderboard_service.get_top_scores()
    user_scores = leaderboard_service.get_user_high_scores(username)

    try:
        background_image = pygame.image.load('assets/Box.jpg')
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except Exception as e:
        print(f"Error loading background image: {e}")
        background_image = None

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BLACK)

        title_surf = font.render("Leaderboard", True, WHITE)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 4, 50))
        screen.blit(title_surf, title_rect)

        for idx, (uname, score) in enumerate(top_scores, start=1):
            score_text = f"{idx}. {uname} - {score}"
            score_surf = font.render(score_text, True, WHITE)
            score_rect = score_surf.get_rect(topleft=(50, 100 + idx * 30))
            screen.blit(score_surf, score_rect)

        user_title_surf = font.render("Your High Scores", True, WHITE)
        user_title_rect = user_title_surf.get_rect(center=(3 * SCREEN_WIDTH // 4, 50))
        screen.blit(user_title_surf, user_title_rect)

        for idx, score in enumerate(user_scores[:10], start=1):
            user_score_text = f"{idx}. {score}"
            user_score_surf = font.render(user_score_text, True, WHITE)
            user_score_rect = user_score_surf.get_rect(topleft=(SCREEN_WIDTH // 2 + 50, 100 + idx * 30))
            screen.blit(user_score_surf, user_score_rect)

        back_button.draw(screen, mouse_pos)
        if back_button.is_clicked(mouse_pos, mouse_pressed):
            return

        pygame.display.flip()
        clock.tick(FPS)

def pause_menu(screen, clock, font):
    button_width = 250
    button_height = 50
    button_spacing = 20
    start_y = SCREEN_HEIGHT // 2 - (button_height + button_spacing)
    try:
        background_image = pygame.image.load('assets/BG.jpg')
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except Exception as e:
        print(f"Error loading background image: {e}")
        background_image = None

    resume_button = Button(
        "Resume Game",
        SCREEN_WIDTH // 2 - button_width // 2,
        start_y,
        button_width,
        button_height,
        WHITE,
        GREY,
        font
    )

    buttons = [resume_button]

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BLACK)

        pause_text = font.render("Paused", True, WHITE)
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, start_y - 60))

        for button in buttons:
            button.draw(screen, mouse_pos)
            if button.is_clicked(mouse_pos, mouse_pressed):
                if button.text == "Resume Game":
                    return GameState.GAME

        pygame.display.flip()
        clock.tick(FPS)
