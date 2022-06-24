import pygame
import math

from game_object import Game_object


class Sheep(Game_object):
    def __init__(self, g_s, screen, skin_name):
        super().__init__(g_s, screen, skin_name)

    def sheep_blit(self):
        self.screen.blit(self.object_img, self.rect)

    def sheep_move_d(self):
        if self.g_settings.left_flag and self.g_settings.top_flag:
            self.g_settings.SPEED = (math.sqrt(2) / 2) * self.g_settings.SPEED
        if self.g_settings.right_flag and self.g_settings.top_flag:
            self.g_settings.SPEED = (math.sqrt(2)/2)*self.g_settings.SPEED
        if self.g_settings.left_flag and self.g_settings.bottom_flag:
            self.g_settings.SPEED = (math.sqrt(2) / 2) * self.g_settings.SPEED
        if self.g_settings.right_flag and self.g_settings.bottom_flag:
            self.g_settings.SPEED = (math.sqrt(2)/2)*self.g_settings.SPEED

    def sheep_move(self):
        if self.g_settings.left_flag:
            self.rect.centerx -= self.g_settings.SPEED
        if self.g_settings.right_flag:
            self.rect.centerx += self.g_settings.SPEED
        if self.g_settings.top_flag:
            self.rect.centery -= self.g_settings.SPEED
        if self.g_settings.bottom_flag:
            self.rect.centery += self.g_settings.SPEED

    def check_wall(self):
        if self.rect.right >= self.sc_rect.right-5:
            self.g_settings.right_flag = False
        if self.rect.left <= self.sc_rect.left+5:
            self.g_settings.left_flag = False

        if self.rect.top <= self.sc_rect.top+5:
            self.g_settings.top_flag = False

        if self.rect.bottom >= self.sc_rect.bottom-5:
            self.g_settings.bottom_flag = False

