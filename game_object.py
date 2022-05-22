import pygame


class Game_object:

    def __init__(self, g_s, screen, skin_name):
        self.g_settings = g_s
        self.screen = screen
        self.object_img = pygame.image.load(f'image/{skin_name}.bmp')
        self.rect = self.object_img.get_rect()
        self.sc_rect = self.screen.get_rect()

        self.center_pos()

    def center_pos(self):
        self.rect.center = self.sc_rect.center
