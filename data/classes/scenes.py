import pygame
import sys
from .add_functions import AdditionalFunctions
from .methods import MainMethods, AdditionalMethods
from .rgb import Colors
from .storage import NamesStorage
from .units import Rooms, AdditionalObjects, Places
from .values import Values

'''
def scene(action):
    def wrapper(cls, win, FPS, clock, player, clock_panel, add_objects):
        go = NamesStorage.action_go
        while go is not NamesStorage.action_stop:
            flat.draw_me()
            flat.render(win)
            flat.room_area.fill(Colors.snow)
            go = action(flat, player, clock_panel, objects, FPS)
            pygame.display.update()
            clock.tick(FPS)
    return wrapper




@scene
def home_action(flat, player, clock_panel, objects, FPS):
    # Проходим по событиям
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.do_action()
                if MainMethods.need_to_get_out(player, flat):
                    return NamesStorage.action_stop
        # Проверяем жив ли игрок
        if player.hp <= 0:
            return NamesStorage.action_stop
        # Счетчик времени
        clock_panel.go()
        # Урон от голода
        AdditionalFunctions.hunger_damage(player, FPS)
        # Отображаем и взаимодействуем с обьектами холодильник и выходная дверь
        MainMethods.render_objects(flat.room_area, player, objects)
        MainMethods.check_objects_responses(flat.room_area, player, objects)
        # Отображаем и взаимодействуем с обьектами игрок и питомцами
        player.make_a_step(flat.room_area)
        MainMethods.render_pets(flat.room_area, player)
        MainMethods.check_own_pets_responses(flat.room_area, player)
        player.show_action(flat.room_area)
        # ВРЕМЯ
        clock_panel.render(flat.room_area)

'''


class WorldScene:
    @classmethod
    def action(cls, win, FPS, clock):
        world = Places.world
        done = True
        while done:
            AdditionalMethods.check_sectors_response(world.sectors, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for sector in world.sectors:
                            if AdditionalMethods.is_mouse_pos_in_area(sector.area, sector.position):
                                return 'go ' + sector.name
            world.render(win)
            pygame.display.update()
            clock.tick(FPS)


class HomeScene:
    @classmethod
    def action(cls, win, FPS, clock, player, clock_panel):
        flat = Rooms.flat_room
        if player.get_in(flat, clock_panel):
            object_dict = flat.objects
            window = object_dict['window']
            table = object_dict['table']
            table.set_position((int(4.5 * Values.wall_width), int(3.2 * Values.floor_height)))
            armchair = object_dict['armchair']
            objects_array = [table, armchair, window]
            # Цикл сценария
            done = True
            while done:
                # Проверяем жив ли игрок
                if player.hp <= 0:
                    pygame.quit()
                    sys.exit()
                # Счетчик времени
                clock_panel.go()
                window.check_time(clock_panel)
                armchair.heal(player, FPS)
                # Урон от голода
                AdditionalFunctions.hunger_damage(player, FPS)
                # Отображаем модельки
                # Собираем квартиру
                flat.draw_me()
                # Отображаем и взаимодействуем с обьектами холодильник и выходная дверь
                MainMethods.render_objects(flat.room_area, player.refrigerators_corner, flat.door, objects_array)
                # Отображаем и взаимодействуем с обьектами игрок и питомцами
                player.make_a_step(flat.room_area, FPS)
                MainMethods.render_pets(flat.room_area, player.pets)
                player.check_response(player.refrigerators_corner, flat.door, player.pets.units, armchair)
                # ВРЕМЯ
                clock_panel.render(flat.room_area)
                # Отображаем квартиру
                flat.render(win)
                # Проходим по событиям
                for event in pygame.event.get():
                    # Выход из игры
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # Что происходит при нажатии на кнопку мыши
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.do_action()
                            # player.drop(flat.room_area)
                            if MainMethods.need_to_get_out(player, flat):
                                done = False
                # Обновляем игровое пространство
                flat.room_area.fill(Colors.snow)
                pygame.display.update()
                clock.tick(FPS)


class MallScene:
    @classmethod
    def action(cls, win, FPS, clock):
        mall = Places.mall_world
        done = True
        while done:
            AdditionalMethods.check_sectors_response(mall.sectors, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for sector in mall.sectors:
                            if AdditionalMethods.is_mouse_pos_in_area(sector.area, sector.position):
                                return 'go ' + sector.name
            mall.render(win)
            pygame.display.update()
            clock.tick(FPS)


class ProductsShopScene:
    @classmethod
    def action(cls, win, FPS, clock, player, clock_panel):
        best_goods_room = Rooms.products_shop_room
        if player.get_in(best_goods_room, clock_panel):
            bob = best_goods_room.objects['cashier']
            basket = best_goods_room.objects['shopping_basket']
            shopping_truck = best_goods_room.objects['shopping_truck']
            food_stand = bob.shop_windows[0]
            mall_objects = [bob, food_stand, best_goods_room.door, basket, shopping_truck]
            basket.set_position((Values.wall_width * 1.4, Values.room_height - Values.floor_height - 35))
            shopping_truck.set_position((Values.wall_width // 2, Values.room_height - Values.floor_height - shopping_truck.area.get_height()//2))
            # Цикл сценария
            done = True
            while done:
                # Проверяем жив ли игрок
                if player.hp <= 0:
                    pygame.quit()
                    sys.exit()
                # Счетчик времени
                clock_panel.go()
                # Урон от голода
                AdditionalFunctions.hunger_damage(player, FPS)
                # Отображаем модельки
                best_goods_room.draw_me()
                MainMethods.render_objects(best_goods_room.room_area, mall_objects)
                bob.show_price()
                MainMethods.check_objects_responses(player, bob, food_stand, best_goods_room.door)
                player.make_a_step(best_goods_room.room_area, FPS)
                #player.show_action(mall_room.room_area)
                # ВРЕМЯ
                #clock_panel.render(mall_room.room_area)
                # Отображаем комнату
                best_goods_room.render(win)
                # Проходим по событиям
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.do_action()
                            #player.do_dynamic_action(mall_objects)
                            player.buy_product(food_stand)
                            if MainMethods.need_to_get_out(player, best_goods_room):
                                done = False
                if not best_goods_room.is_opened(clock_panel):
                    done = False
                # Очищаем пространство комнаты
                best_goods_room.room_area.fill(Colors.snow)
                pygame.display.update()
                clock.tick(FPS)


class PetsShopScene:
    @classmethod
    def action(cls, win, FPS, clock, player, clock_panel):
        pets_shop_room = Rooms.pets_shop_room
        if player.get_in(pets_shop_room, clock_panel):
            pets_house = pets_shop_room.objects['pets_house']
            cat_house = pets_shop_room.objects['cat_house']
            dog_house = pets_shop_room.objects['dog_house']
            susan = pets_shop_room.objects['animal_seller']
            window = pets_shop_room.objects['window']
            pets_house.set_position((Values.wall_width * 4.5, Values.room_height - Values.floor_height - pets_house.area.get_height()))
            cat_house.set_position((Values.wall_width + cat_house.area.get_width() // 8, Values.room_height - Values.floor_height - cat_house.area.get_height() ))
            dog_house.set_position((Values.wall_width - dog_house.area.get_width() // 1.5, Values.room_height - Values.floor_height - dog_house.area.get_height() // 3))
            objects_array = [pets_house, susan, pets_house, window, cat_house, dog_house]
            # Цикл сценария
            done = True
            while done:
                # Проверяем жив ли игрок
                if player.hp <= 0:
                    pygame.quit()
                    sys.exit()
                # Счетчик времени
                clock_panel.go()
                # Урон от голода
                AdditionalFunctions.hunger_damage(player, FPS)
                # Отображаем модельки
                Rooms.pets_shop_room.draw_me()
                MainMethods.render_objects(Rooms.pets_shop_room.room_area, objects_array, pets_shop_room.door)
                MainMethods.check_objects_responses(player, susan.pets.units, pets_shop_room.door)
                #player.check_response(susan.pets.units, pets_shop_room.door)
                susan.show_price()
                susan.response()
                window.check_time(clock_panel)
                player.make_a_step(Rooms.pets_shop_room.room_area, FPS)
                MainMethods.render_pets(Rooms.pets_shop_room.room_area, susan.pets)
                # ВРЕМЯ
                # Отображаем комнату
                Rooms.pets_shop_room.render(win)
                # Проходим по событиям
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.do_action()
                            player.buy_pet(susan)
                            # player.do_dynamic_action(susan_pets_objects)
                            if MainMethods.need_to_get_out(player, Rooms.pets_shop_room):
                                done = False
                if not pets_shop_room.is_opened(clock_panel):
                    done = False
                # Очищаем пространство комнаты
                Rooms.pets_shop_room.room_area.fill(Colors.snow)
                pygame.display.update()
                clock.tick(FPS)


class WorkScene:
    @classmethod
    def action(cls, win, FPS, clock, player, clock_panel):
        office = Rooms.office
        if player.get_in(office, clock_panel):
            player.render(office.room_area)
            objects_dict = office.objects
            work_desk = objects_dict['desk']
            football_table = objects_dict['football_table']
            coffee_machine = objects_dict['coffee_machine']
            office_objects = [office.door, work_desk, football_table, coffee_machine]
            # Главный цикл игры
            seconds = 0
            done = True
            while done:
                # Проверяем жив ли игрок
                if player.hp <= 0:
                    pygame.quit()
                    sys.exit()
                # Счетчик времени
                seconds += 1 / FPS
                clock_panel.go()
                # Урон
                AdditionalFunctions.hunger_damage(player, FPS)
                # Отображаем модельки
                office.draw_me()
                MainMethods.render_objects(office.room_area, office_objects)

                player.check_response(office_objects)
                player.do_static_action(FPS, NamesStorage.work, work_desk)
                player.make_a_step(office.room_area, FPS)
                # ВРЕМЯ
                clock_panel.render(office.room_area)
                # Всплывающие деньги
                AdditionalObjects.dollar_gun.run(office.room_area, FPS)
                # Отображаем комнату
                office.render(win)
                # Проходим по событиям
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.do_action()
                            player.catch_money(AdditionalObjects.dollar_gun)
                            player.get_coffee(coffee_machine)
                            player.play_table_football(football_table)
                            if MainMethods.need_to_get_out(player, office):
                                done = False
                if not office.is_opened(clock_panel):
                    done = False
                # Очищаем пространство комнаты
                office.room_area.fill(Colors.snow)
                pygame.display.update()
                clock.tick(FPS)


class ClubScene:
    @classmethod
    def action(cls, win, FPS, clock, player, clock_panel):
        club = Rooms.club_room
        if player.get_in(club, clock_panel):
            objects_dict = club.objects
            player.render(club.room_area)
            bar = objects_dict['bar']
            disco_ball = objects_dict['disco_ball']
            left_speaker = objects_dict['left_speaker']
            right_speaker = objects_dict['right_speaker']
            eva = objects_dict['eva']
            adam = objects_dict['adam']
            bitch = objects_dict['bitch']
            disco_ball.set_position(( (Values.room_width - disco_ball.area.get_width()) // 2, Values.roof_height // 5 ))
            left_speaker.set_position((Values.wall_width * 1.1, Values.room_height - Values.floor_height - left_speaker.get_height()))
            right_speaker.set_position((Values.wall_width * 3.7, Values.room_height - Values.floor_height - left_speaker.get_height()))
            eva.set_position((Values.wall_width * 4.3, Values.room_height - Values.floor_height * 2.2))
            adam.set_position((Values.wall_width * 5, Values.room_height - Values.floor_height * 2))

            club_objects = [club.door, bar, disco_ball, left_speaker, right_speaker, eva, adam, bitch]

            # music
            pygame.mixer.music.load('sounds/night_club.mp3')
            pygame.mixer.music.play()

            # Главный цикл игры
            seconds = 0
            done = True
            while done:
                # Проверяем жив ли игрок
                if player.hp <= 0:
                    pygame.quit()
                    sys.exit()
                # Счетчик времени
                seconds += 1 / FPS
                clock_panel.go()
                # Урон
                AdditionalFunctions.hunger_damage(player, FPS)
                # Отображаем модельки
                club.draw_me()
                MainMethods.render_objects(club.room_area, club_objects)
                player.check_response(club.door, bar, bitch)
                player.make_a_step(club.room_area, FPS)
                bitch.check_mood()
                # ВРЕМЯ
                clock_panel.render(club.room_area)
                # Отображаем комнату
                club.render(win)
                # Проходим по событиям
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.do_action()
                            player.buy_alcohol(bar)
                            player.get_the_bitch_drunk(bitch)
                            if MainMethods.need_to_get_out(player, club):
                                pygame.mixer.music.pause()
                                done = False
                            if player.fuck_bitch(bitch, clock_panel):
                                done = False
                if not club.is_opened(clock_panel):
                    pygame.mixer.music.pause()
                    done = False
                # Очищаем пространство комнаты
                club.room_area.fill(Colors.snow)
                pygame.display.update()
                clock.tick(FPS)


class Scenes:
    home_scene = HomeScene()
    products_shop_scene = ProductsShopScene()
    world_scene = WorldScene()
    work_scene = WorkScene()
    mall_scene = MallScene()
    pets_shop_scene = PetsShopScene()
    club_scene = ClubScene()



