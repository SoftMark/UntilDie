import pygame
from classes.units import Player, Places, Panels, Rooms, MPC, Refrigerators, AdditionalObjects, Panels
from classes.display import Display
from classes.scenes import HomeScene, ProductsShopScene, WorldScene, WorkScene, MallScene, PetsShopScene, ClubScene

mike = Player.player
mike.refrigerators_corner.append(Refrigerators.saturn)
game_clock = Panels.clock_panel
flat = Rooms.flat_room
office = Rooms.office
products_shop = Rooms.products_shop_room
pets_shop = Rooms.pets_shop_room
club = Rooms.club_room


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
while done:

    go = WorldScene.action(win, Places.world, FPS, clock)

    if go == 'go home':
        if mike.get_in(flat, game_clock):
            HomeScene.action(win, FPS, clock, mike, flat, game_clock, [])

    elif go == 'go mall':
        while True:
            go = MallScene.action(win, Places.mall_world, FPS, clock)
            if go == 'go Best-goods':
                if mike.get_in(products_shop, game_clock):
                    ProductsShopScene.action(win, FPS, clock, mike, products_shop, game_clock, [])
            elif go == "go Susan's pets":
                if mike.get_in(pets_shop, game_clock):
                    PetsShopScene.action(win, FPS, clock, mike, game_clock, pets_shop)
            elif go == 'go exit':
                break

    elif go == 'go work':
        if mike.get_in(office, game_clock):
            WorkScene.action(win, FPS, clock, mike, office, game_clock, [])

    elif go == 'go club':
        if mike.get_in(club, game_clock):
            ClubScene.action(win, FPS, clock, mike, club, game_clock, [])

    pygame.display.update()
    clock.tick(FPS)