class Settings:

    def __init__(self):

        self.GAME_RUN = True
        self.FPS = 60
        self.SPEED = 5

        self.sheep_speed_left = self.SPEED
        self.sheep_speed_right = self.SPEED
        self.sheep_speed_top = self.SPEED
        self.sheep_speed_bottom = self.SPEED

        self.left_flag = False
        self.right_flag = False
        self.top_flag = False
        self.bottom_flag = False


