import pygame
import functions as f

from settings import Settings
from sheep import Sheep
from game_object import Game_object


def main():
    pygame.init()

    def run_game():
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Овечьи бои')
        bk_game = pygame.image.load('image/bk_game.bmp')
        screen_rect = screen.get_rect()
        g_settings = Settings()
        Game_object(g_settings, screen, skin_name='sheep_W')
        sheep = Sheep(g_settings, screen, 'sheep_W')

        while True:

            f.check_events(g_settings)

            sheep.check_wall()

            sheep.sheep_move()

            f.screen_update(screen, screen_rect, bk_game, sheep)
            clock.tick(g_settings.FPS)

    run_game()


if __name__ == '__main__':
    main()
