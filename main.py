import pygame
import functions as f

from settings import Settings
from sheep import Sheep
from apple import Apple
from game_object import Game_object


def main():
    pygame.init()

    def run_game():
        clock = pygame.time.Clock()
        g_settings = Settings()
        screen = pygame.display.set_mode((g_settings.W, g_settings.H))
        pygame.display.set_caption('Овечьи бои')
        bk_game = pygame.image.load('image/bk_game.bmp')
        screen_rect = screen.get_rect()
        Game_object(g_settings, screen, skin_name='sheep_W')
        sheep = Sheep(g_settings, screen, 'sheep_W')

        apple1 = Apple(g_settings, screen, 'apple')
        apple2 = Apple(g_settings, screen, 'apple')
        apple3 = Apple(g_settings, screen, 'apple')

        while True:

            f.check_events(g_settings)
            sheep.check_wall()
            #sheep.sheep_move_d()
            sheep.sheep_move()

            f.screen_update(screen, screen_rect, bk_game, sheep, apple1)
            clock.tick(g_settings.FPS)

    run_game()


if __name__ == '__main__':
    main()
