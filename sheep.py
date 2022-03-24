import pygame


class Sheep:

    def __init__(self, g_s, screen):

        self.g_settings = g_s

        self.sheep_img = pygame.image.load('image/sheep_W.bmp')
        self.rect = self.sheep_img.get_rect()
        self.screen = screen
        self.sc_rect = self.screen.get_rect()

        self.rect.centerx = float(self.sc_rect.centerx)
        self.rect.centery = float(self.sc_rect.centery)

    def sheep_move(self):  # ========================================================================================

        self.rect.centerx += self.g_settings.sheep_sp_x
        self.rect.centery += self.g_settings.sheep_sp_y

    def sheep_blit(self):
        self.screen.blit(self.sheep_img, self.rect)

    def check_wall(self):
        if self.rect.right >= self.sc_rect.right:
            self.g_settings.right_flag = False
        else:
            self.g_settings.right_flag = True
        if self.rect.left <= self.sc_rect.left:
            self.g_settings.left_flag = False
        else:
            self.g_settings.left_flag = True

        if self.rect.top <= self.sc_rect.top:
            self.g_settings.top_flag = False
        else:
            self.g_settings.top_flag = True

        if self.rect.bottom >= self.sc_rect.bottom:
            self.g_settings.bottom_flag = False
        else:
            self.g_settings.bottom_flag = True