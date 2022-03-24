import pygame


def screen_update(screen, rect, bk_pict, sheep):  # Функция отрисовки экрана
    screen.blit(bk_pict, rect)  # заливка фона экрана
    sheep.sheep_blit()  # рисование овцы поверх экрана
    pygame.display.update()  # Перворачивание (обновление) всего экрана


def check_events(g_settings):  # Проверка внутриигровых событий
    for event in pygame.event.get():  # цикл проверки внутриигрвых событий
        if event.type == pygame.QUIT:  # проверка нажания на кнопку выхода (красный крест)
            exit()  # Завершение работы приложения

        elif event.type == pygame.KEYDOWN:  # проверка нажания на кнопку
            if event.key == pygame.K_RIGHT:
                if g_settings.right_flag:
                    g_settings.sheep_sp_x = 1
            if event.key == pygame.K_LEFT:
                if g_settings.left_flag:
                    g_settings.sheep_sp_x = -1
            if event.key == pygame.K_UP:
                if g_settings.top_flag:
                    g_settings.sheep_sp_y = -1
            if event.key == pygame.K_DOWN:
                if g_settings.bottom_flag:
                    g_settings.sheep_sp_y = 1

        elif event.type == pygame.KEYUP:   # проверк отжатия кнопки
            if event.key == pygame.K_RIGHT:
                g_settings.sheep_sp_x = 0
            if event.key == pygame.K_LEFT:
                g_settings.sheep_sp_x = 0
            if event.key == pygame.K_UP:
                g_settings.sheep_sp_y = 0
            if event.key == pygame.K_DOWN:
                g_settings.sheep_sp_y = 0
