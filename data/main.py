import pygame
from ud_classes.units import Player, Refrigerators, Panels
from ud_classes.display import Display
from ud_classes.scenes import Scenes


mike = Player.player
mike.refrigerators_corner.append(Refrigerators.saturn)
mike.money = 500
game_clock = Panels.clock_panel

# Pygame
pygame.init()
# Игровое окно
win = Display.create_window()
# Дальше будем указывать количество кадров в секунду
FPS = 60
clock = pygame.time.Clock()
# Главный цикл игры
seconds = 0
done = True
go = 'go home'
while done:
    if go == 'go home':
        Scenes.home_scene.action(win, FPS, clock, mike, game_clock)

    elif go == 'go mall':
        while True:
            go = Scenes.mall_scene.action(win, FPS, clock)
            if go == 'go Best-goods':
                Scenes.products_shop_scene.action(win, FPS, clock, mike, game_clock)
            elif go == "go Susan's pets":
                Scenes.pets_shop_scene.action(win, FPS, clock, mike, game_clock)
            elif go == 'go exit':
                break

    elif go == 'go work':
        Scenes.work_scene.action(win, FPS, clock, mike, game_clock)

    elif go == 'go club':
        Scenes.club_scene.action(win, FPS, clock, mike, game_clock)

    go = Scenes.world_scene.action(win, FPS, clock)

    pygame.display.update()
    clock.tick(FPS)
