class Settings:

    def __init__(self):
        self.W = 800  # ширина экрана
        self.H = 600  # высота экрана
        self.GAME_RUN = True  # ключ начала основного игрового цикла
        self.FPS = 60  # частота кадров
        self.SPEED = 5  # скорость перемещения игрового персонажа

        # Флаги переключения направления движения игрового персонажа

        self.left_flag = False
        self.right_flag = False
        self.top_flag = False
        self.bottom_flag = False


