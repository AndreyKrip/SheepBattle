import pygame
import functions as f

from settings import Settings
from sheep import Sheep


def main():
    pygame.init()

    def run_game():
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Овечьи бои')
        bk_game = pygame.image.load('image/bk_game.bmp')
        screen_rect = screen.get_rect()
        g_settings = Settings()
        sheep = Sheep(g_settings, screen)

        while True:
            sheep.check_wall()
            f.check_events(g_settings)
            sheep.sheep_move()
            f.screen_update(screen, screen_rect, bk_game, sheep)

    run_game()


if __name__ == '__main__':
    main()
