from game_object import Game_object
import random


class Apple(Game_object):

    def __init__(self, g_s, screen, skin_name):
        super().__init__(g_s, screen, skin_name)
        self.center_pos()

    def apple_blit(self):
        self.screen.blit(self.object_img, self.rect)

    def center_pos(self):
        self.rect.centerx = self.sc_rect.centerx + random.randint(-300, 300)
        self.rect.centery = self.sc_rect.centery + random.randint(-300, 300)
