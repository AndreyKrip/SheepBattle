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
                g_settings.right_flag = True
            elif event.key == pygame.K_LEFT:
                g_settings.left_flag = True
            elif event.key == pygame.K_UP:
                g_settings.top_flag = True
            elif event.key == pygame.K_DOWN:
                g_settings.bottom_flag = True

        elif event.type == pygame.KEYUP:   # проверк отжатия кнопки
            if event.key == pygame.K_RIGHT:
                g_settings.right_flag = False
            elif event.key == pygame.K_LEFT:
                g_settings.left_flag = False
            elif event.key == pygame.K_UP:
                g_settings.top_flag = False
            elif event.key == pygame.K_DOWN:
                g_settings.bottom_flag = False




