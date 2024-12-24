import pygame
from game.constants import *
import sys

def get_username(screen, clock):
    """
    Prompts the player to enter their username before starting the game.
    Background is white and the input box and text are both black.
    """
    username = ""
    input_active = True

    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20, 200, 40)
    font = pygame.font.Font(None, 36)
    # Set both colors to black
    color_inactive = BLACK
    color_active = BLACK
    color = color_inactive
    active = False

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if username.strip() == "":
                            username = "Player" # default if empty
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) < 20:
                            username += event.unicode

        screen.fill(WHITE)
        prompt_text = font.render("Username:", True, BLACK)
        screen.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, SCREEN_HEIGHT // 2 - 60))

        # Always render text in black
        txt_surface = font.render(username, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Draw a black rectangle for the box border
        pygame.draw.rect(screen, BLACK, input_box, 2)
        # Blit the text in black
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()
        clock.tick(30)

    return username if username.strip() != "" else "Player"
