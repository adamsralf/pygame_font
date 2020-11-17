import pygame
from pygame.constants import (
    QUIT, K_ESCAPE, KEYDOWN, KEYUP, K_KP_PLUS, K_KP_MINUS, K_r, K_g, K_b, KMOD_LSHIFT
)
import os


class Settings:
    """Project global informations.

    This static class contains project global informations 
    like window size and file directories.
    """
    window_width = 700
    window_height = 300

    @staticmethod
    def get_dim():
        """Gets window width and height as a pair.

        Returns:
            list: (window_width, window_height)
        """
        return (Settings.window_width, Settings.window_height)


if __name__ == '__main__':
    # Preparation
    os.environ['SDL_VIDEO_WINDOW_POS'] = "500, 150"

    #pylint: disable=no-member
    pygame.init()
    #pylint: enable=no-member
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Settings.get_dim())

    fontsize = 24
    fontcolor = [255, 255, 255]

    # main loop
    running = True
    font = pygame.font.Font(pygame.font.get_default_font(), fontsize)
    text = font.render("Hello World!", True, fontcolor)

    print(f"size={fontsize}, r={fontcolor[0]}, g={fontcolor[1]}, b={fontcolor[2]} ")

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_KP_PLUS:
                    fontsize += 1
                elif event.key == K_KP_MINUS:
                    fontsize -= 1
                elif event.key == K_r:
                    if event.mod & KMOD_LSHIFT:
                        fontcolor[0] = (fontcolor[0] - 5) % 256
                    else: 
                        fontcolor[0] = (fontcolor[0] + 5) % 256
                elif event.key == K_g:
                    if event.mod & KMOD_LSHIFT:
                        fontcolor[1] = (fontcolor[1] - 5) % 256
                    else: 
                        fontcolor[1] = (fontcolor[1] + 5) % 256
                elif event.key == K_b:
                    if event.mod & KMOD_LSHIFT:
                        fontcolor[2] = (fontcolor[2] - 5) % 256
                    else: 
                        fontcolor[2] = (fontcolor[2] + 5) % 256
                font = pygame.font.Font(pygame.font.get_default_font(), fontsize)
                text = font.render("Hello World!", True, fontcolor)
                print(f"size={fontsize}, r={fontcolor[0]}, g={fontcolor[1]}, b={fontcolor[2]} ")

        # draw
        screen.fill((0, 0, 0))
        screen.blit(text, (Settings.window_width//2 - text.get_rect().centerx, Settings.window_height//2 - text.get_rect().centery))
        pygame.display.flip()

    #pylint: disable=no-member
    pygame.quit()
    #pylint: enable=no-member
