from .rgb import Colors
from .values import Values
from .storage import NamesStorage
from .methods import AdditionalMethods, MainMethods
from .add_functions import AdditionalFunctions
from .sounds import MainSounds
from .display import ChoicePanel, HPPanel, CashPanel
from .objects import UnitStorage
from .body_parts import Hand, Face
from .key_set import *

import random
import pygame


class Animal:
    # Инициализирует животное
    def __init__(self, name, hp, kind, x_pos, y_pos, sprites, voice):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.kind = kind
        self.x = x_pos
        self.y = y_pos
        # Выгружает картинку
        self.sprites = sprites
        self.bitmap = self.sprites.bitmap
        self.area = AdditionalMethods.create_panel_area((self.bitmap.get_width(), self.bitmap.get_height()))
        self.hp_panel = HPPanel()
        # Какой цвет изображения делать прозрачным
        #self.bitmap.set_colorkey((0, 0, 0))
        self.area.set_colorkey(Colors.snow)
        self.top_panel = ChoicePanel("Text", Colors.black, Colors.black, (0, 0))
        self.top_panel_distance = 20
        self.top_panel.invisible()
        self.voice = voice

    # Отображает на игровом пространстве
    def render(self, screen):
        self.area.fill(Colors.snow)
        self.hp_panel.render(self.bitmap, self.hp, self.max_hp, Colors.black)
        self.set_top_panel_position()
        self.top_panel.render(screen)
        self.area.blit(self.bitmap, (0, 0))
        screen.blit(self.area, (self.x, self.y))

    # Ням - ням
    def eat(self, food):
        if 'drink' in food.kind:
            self.voice.drink.play()
        else:
            self.voice.chewing.play()
        self.hp += food.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_top_panel_position(self):
        self.top_panel.x = self.x + AdditionalFunctions.minus_half(self.bitmap.get_width(),
                                                                   self.top_panel.area.get_width())
        self.top_panel.y = self.y - self.top_panel_distance - self.top_panel.area.get_height()

    def show_top_panel(self):
        self.top_panel.visible()

    def hide_top_panel(self):
        self.top_panel.invisible()

    def response(self):
        self.show_top_panel()

    def sleep(self):
        self.hide_top_panel()


class Pet(Animal):
    def __init__(self, name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice):
        super().__init__(name, hp, kind, x_pos, y_pos, sprites, voice)
        self.step = step
        self.breed = breed
        self.price = price
        self.top_panel.change_text("Buy")

    def render(self, screen):
        if self.hp > 0:
            if self.hp == self.max_hp:
                self.top_panel.change_text('Buy')
            elif self.hp > 0.8 * self.max_hp:
                self.top_panel.change_text('Play')
            else:
                self.top_panel.change_text('Feed')
        else:
            self.top_panel.change_text('Bury')

        self.set_top_panel_position()
        self.top_panel.render(screen)
        self.area.fill(Colors.snow)
        self.hp_panel.transparent()
        self.area.blit(self.bitmap, (0, 0))
        if self.hp > 0:
            self.hp_panel.render(self.area, self.hp, self.max_hp, Colors.black)
        screen.blit(self.area, (self.x, self.y))

    def make_a_random_step(self, screen):
        random_value = random.randrange(0, 200)
        if random_value == 1 and self.x < Values.room_width - Values.wall_width - self.bitmap.get_width() // 2:
            self.x += self.step
        elif random_value == 2 and self.x > Values.wall_width - self.bitmap.get_width() // 2:
            self.x -= self.step
        elif random_value == 3 and self.y > Values.room_height - Values.floor_height - self.bitmap.get_height() // 5 * 4:
            self.y -= self.step
        elif random_value == 4 and self.y < Values.room_height - self.bitmap.get_height() - 20:
            self.y += self.step
        self.render(screen)


class Dog(Pet):
    def __init__(self, name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice):
        super().__init__(name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice)
        self.hp_panel.adapt_for_unit(self.bitmap, 0.38, 0.44)
        self.kind = 'dog'
        #self.hp_panel.transparent()


class Cat(Pet):
    def __init__(self, name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice):
        super().__init__(name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice)
        self.hp_panel.adapt_for_unit(self.bitmap, 0.32, 0.40)
        self.kind = 'cat'
        #self.hp_panel.transparent()


class Human(Animal):
    he_she = 'It'
    his_her = 'Its'
    salary = 5.25
    max_salary = 12
    money = 10
    step = 500
    mood = 70
    max_mood = 100
    animation_counter = 1
    damage = 25

    def __init__(self, name, gender, kind, hp, x_pos, y_pos, sprites, voice):
        super().__init__(name, hp, kind, x_pos, y_pos, sprites, voice)
        # Gender things
        self.gender = gender
        # Body parts
        self.face = Face()
        self.face.adapt(self.bitmap)
        left_hand = Hand('left hand', 1, [])
        right_hand = Hand('right hand', 1, [])
        self.hands = [left_hand, right_hand]
        # Storage
        self.refrigerators_corner = []
        self.pets = UnitStorage('pets', 3, [])
        self.kind = 'human'
        self.cash_panel = CashPanel()
        self.cash_panel.adapt_for_unit(self.bitmap, 0.45, 0.33)
        self.hp_panel.adapt_for_unit(self.bitmap, 0.5, 0.28)
        self.top_panel.change_text("Eat")

    # Main

    def check_response(self, *responsers):
        for responser in responsers:
            if type(responser) == list:
                array = responser
                for resp in array:
                    self.check_response(resp)
            else:
                if AdditionalMethods.is_in_response_range(responser, self):
                    responser.response()
                else:
                    responser.sleep()

    def render(self, screen):
        # AdditionalMethods.draw_surface_box(self.area, Colors.toxic)
        # AdditionalMethods.draw_surface_box(self.sprites.top, Colors.red)
        # AdditionalMethods.draw_surface_box(self.bitmap, Colors.red)
        # screen.blit(self.sprites.top, (300, 0))
        self.check_mood()
        self.area.blit(self.sprites.head, (3, 0))
        self.area.blit(self.sprites.body, (3, 43))

        # screen.blit(self.bitmap, (300, 200))
        self.set_top_panel_position()
        self.check_hands()
        self.draw_me()
        self.render_panels(screen)
        self.render_hands(screen)
        screen.blit(self.area, (self.x, self.y))

    def draw_me(self):
        self.face.draw_me(self.area, AdditionalFunctions.get_current_hp_color(self.hp, self.max_hp), self.mood)

    def render_hands(self, screen):
        self.hands[0].render(screen, (self.x, self.y), (0, self.bitmap.get_height() // 2))
        self.hands[1].render(screen, (self.x, self.y), (self.bitmap.get_width() - Values.hand_panel_width,
                                                        self.bitmap.get_height() // 2))

    def render_panels(self, screen):
        if not self.is_hands_empty():
            full_hand = self.get_full_hand()
            if 'drink' in full_hand.units[0].kind:
                self.top_panel.change_text('Drink')
            else:
                self.top_panel.change_text('Eat')
        self.top_panel.render(screen)
        self.hp_panel.render(self.area, self.hp, self.max_hp, Colors.black)
        self.cash_panel.render(self.area, self.money)

    def make_a_step(self, screen, FPS):
        self.area.fill(Colors.snow)
        legs_sprites = self.sprites.walk_legs
        keys = Actions(pygame.key.get_pressed())
        if keys.right or keys.left or keys.down or keys.up:
            if keys.right and self.x < Values.room_width - Values.wall_width - self.bitmap.get_width() // 2:
                self.x += self.step
            elif keys.left and self.x > Values.wall_width - self.bitmap.get_width() // 2:
                self.x -= self.step
            elif keys.down and self.y > Values.room_height - Values.floor_height - self.bitmap.get_height() // 5 * 4:
                self.y -= self.step
            elif keys.up and self.y < Values.room_height - self.bitmap.get_height() - 20:
                self.y += self.step

            if self.animation_counter + 1 >= FPS:
                self.animation_counter = 0
                self.voice.foot_step.play()
            if self.animation_counter / (FPS // len(legs_sprites)) % 1 == 0:
                self.voice.foot_step.play()
            self.area.blit(legs_sprites[self.animation_counter // (FPS // len(legs_sprites))], (-50, 0))
            self.animation_counter += 1
        else:
            self.area.blit(self.sprites.legs, (-50, 0))
            self.animation_counter = 0
        self.render(screen)

    def dance(self, FPS):
        pass

    def do_action(self):
        self.actions_with_refrigerators()
        self.actions_with_food()
        self.pets_actions()

    def do_static_action(self, FPS, action_name, *carriers):
        for carrier in carriers:
            if AdditionalMethods.is_in_response_range(self, carrier):
                if action_name == NamesStorage.work:
                    self.work(FPS)

    def buy_product(self, products_stand):
        try:
            if self.buy(products_stand.get_stuff()):
                products_stand.sounds.pik.play()
            else:
                self.say_nuh()
        except:
            pass

    def buy_pet(self, animal_seller):
        try:
            pet = animal_seller.get_pet()
            if AdditionalMethods.is_in_response_range(self, pet):
                if self.buy(pet):
                    random_x = random.randrange(Values.wall_width,
                                                Values.room_width - Values.wall_width - pet.area.get_width())
                    random_y = random.randrange(Values.room_height - Values.floor_height - pet.area.get_height(),
                                                Values.room_height - pet.area.get_height())
                    pet.x = random_x
                    pet.y = random_y
                    pet.voice.play.play()
                else:
                    self.say_nuh()
        except:
            pass

    def buy_alcohol(self, bar):
        try:
            alcohol = bar.generate_alcohol()
            if AdditionalMethods.is_in_response_range(bar, self):
                if AdditionalMethods.is_mouse_pos_in_area(bar.top_panel.area, bar.top_panel.get_position()):
                    if self.have_i_free_hand():
                        if self.money >= alcohol.price:
                            self.money -= alcohol.price
                            hand = self.get_free_hand()
                            AdditionalFunctions.put_unit_to_place_holder(alcohol, hand)
                        else:
                            self.say_nuh()
                    else:
                        self.say_nuh()
        except:
            pass

    def get_coffee(self, coffee_machine):
        if AdditionalMethods.is_in_response_range(coffee_machine, self):
            if AdditionalMethods.is_mouse_pos_in_top_panel_area(coffee_machine):
                if self.money >= coffee_machine.coffee_price:
                    self.money -= coffee_machine.coffee_price
                    self.add_m_mood()
                    coffee_machine.talk(coffee_machine.sounds.get_coffee)
                else:
                    self.say_nuh()

    def play_table_football(self, table_football):
        if AdditionalMethods.is_in_response_range(table_football, self):
            if AdditionalMethods.is_mouse_pos_in_top_panel_area(table_football):
                self.add_m_mood()
                self.hp -= 0.05 * self.max_hp
                table_football.talk(table_football.sounds.play_table_football)

    def get_the_bitch_drunk(self, bitch):
        if AdditionalMethods.is_in_response_range(bitch, self):
            if AdditionalMethods.is_mouse_pos_in_top_panel_area(bitch):
                if bitch.top_panel.text == 'Drink':
                    if self.is_hands_empty():
                        self.voice.nuh.play()
                        return
                    # hands are not empty
                    for hand in self.hands:
                        # left hand is empty
                        if self.is_hand_empty(hand):
                            continue
                        else:
                            if 'alcohol' in hand.units[0].kind:
                                bitch.drink()
                                bitch.voice.drink.play()
                                del hand.units[0]
                                return
                    self.voice.nuh.play()

    def fuck_bitch(self, bitch, clock):
        if AdditionalMethods.action_with_unit(self, bitch):
            if bitch.top_panel.text == 'Sex':
                bitch.voice.pleasure.play()
                bitch.mood = 0
                self.full_mood()
                left_hand = self.hands[0]
                if not self.is_hand_empty(left_hand):
                    del left_hand.units[0]
                right_hand = self.hands[1]
                if not self.is_hand_empty(right_hand):
                    del right_hand.units[0]
                clock.hours = 12
                clock.minutes = 0
                return True
        return False

    def catch_money(self, dollar_gun):
        try:
            dollar = dollar_gun.current_dollar
            if AdditionalMethods.is_mouse_pos_in_area(dollar.area, dollar.get_position()):
                self.money += dollar.value
                dollar_gun.drop_money()
        except:
            pass

    def get_in(self, room, clock):
        if room.is_opened(clock):
            room.door.talk(room.door.sounds.open)
            self.x = room.door.x + room.door.area.get_width() // 2
            self.y = room.door.y + room.door.area.get_height() // 5
            return True
        else:
            MainSounds.nuh.play()
            return False

    # Hands

    def get_from_hands(self):
        for hand in self.hands:
            if not self.is_hand_empty(hand):
                thing = self.get_from_hand(hand)
                return thing

    @classmethod
    def get_from_hand(cls, hand):
        thing = hand.units[0]
        del hand.units[0]
        return thing

    def is_hands_empty(self):
        answer = True
        for hand in self.hands:
            if not self.is_hand_empty(hand):
                answer = False
        return answer

    @classmethod
    def is_hand_empty(cls, hand):
        if len(hand.units) > 0:
            return False
        else:
            return True

    def free_hand(self):
        pass

    def have_i_free_hand(self):
        answer = False
        for hand in self.hands:
            if len(hand.units) == 0:
                answer = True
        return answer

    def get_free_hand(self):
        for hand in self.hands:
            if len(hand.units) == 0:
                return hand

    def get_full_hand(self):
        for hand in self.hands:
            if len(hand.units) != 0:
                return hand

    def drop(self, where):
        if not self.is_hands_empty():
            hand = self.get_full_hand()
            thing = self.get_from_hand(hand)
            position_to_drop = (Values.room_width - self.x,
                                Values.room_height - self.y + self.bitmap.get_height())
            thing.render(where, position_to_drop)

    def check_hands(self):
        if not self.is_hands_empty() and AdditionalFunctions.are_they_closed(self.refrigerators_corner):
            self.show_top_panel()
        else:
            self.hide_top_panel()

    # Refrigerator

    def actions_with_refrigerators(self):
        for refrigerator in self.refrigerators_corner:
            if AdditionalMethods.is_in_response_range(refrigerator, self):
                self.decide_to_open_close_refrigerator(refrigerator)
                self.take_product(refrigerator)

    @classmethod
    def decide_to_open_close_refrigerator(cls, refrigerator):
        if AdditionalMethods.is_mouse_pos_in_area(refrigerator.top_panel.area, refrigerator.top_panel.get_position()):
            refrigerator.change_condition()

    def take_product(self, refrigerator):
        if refrigerator.condition == NamesStorage.opened:
            if AdditionalMethods.is_mouse_pos_in_area(refrigerator.area, refrigerator.get_position()):
                if not AdditionalFunctions.is_place_holder_empty(refrigerator):
                    if self.have_i_free_hand():
                        try:
                            product = refrigerator.get_product()
                            AdditionalFunctions.put_unit_to_place_holder(product, self.get_free_hand())
                        except:
                            pass
                    else:
                        self.voice.nuh.play()

    # Food

    def decide_to_eat(self):
        if AdditionalFunctions.are_they_closed(self.refrigerators_corner):
            if AdditionalMethods.is_mouse_pos_in_area(self.top_panel.area, self.top_panel.get_position()):
                return True

    def actions_with_food(self):
        if not self.is_hands_empty():
            if self.decide_to_eat():
                food = self.get_from_hands()
                self.eat(food)
                if food.kind == "alcohol-drink":
                    self.add_l_mood()
                else:
                    self.add_s_mood()

    # Pets

    def pets_actions(self):
        i = 0
        for pet in self.pets.units:
            if AdditionalMethods.is_in_response_range(self, pet):
                if AdditionalMethods.is_mouse_pos_in_area(pet.top_panel.area,
                                                          pet.top_panel.get_position()):
                    if pet.top_panel.text == 'Feed':
                        self.decide_to_feed(pet)
                        return
                    elif pet.top_panel.text == 'Play':
                        self.decide_to_pet(pet)
                        return
                    elif pet.top_panel.text == 'Bury':
                        MainSounds.rip_bell.play()
                        del self.pets.units[i]
                        return
                elif AdditionalMethods.is_mouse_pos_in_area(pet.area, (pet.x, pet.y)):
                    self.decide_to_hit(pet)
                    return
            i += 1

    def decide_to_pet(self, pet):
        pet.hp -= pet.max_hp * 0.05
        self.add_m_mood()
        pet.voice.play.play()

    def decide_to_hit(self, pet):
        # Do not hit the grave
        if pet.hp == 0:
            self.voice.nuh.play()
            return

        pet.voice.scream.play()
        if pet.hp < self.damage:
            pet.hp = 0
        else:
            pet.hp -= self.damage
        return

    def decide_to_feed(self, pet):
        if self.is_hands_empty():
            self.voice.nuh.play()
            return
        # hands are not empty
        for hand in self.hands:
            # left hand is empty
            if self.is_hand_empty(hand):
                continue
            else:
                if AdditionalFunctions.is_food_for_animal(pet, hand.units[0]):
                    food = self.get_from_hand(hand)
                    pet.eat(food)
                    return
        self.voice.nuh.play()

    # Work and buy

    def work(self, FPS):
        self.money += self.salary / FPS / 30
        self.salary += 0.25 / FPS
        self.mood -= self.salary / FPS / 15
        self.hp -= self.salary / FPS / 15
        if self.mood < 0:
            self.mood = 0

    def buy(self, stuff):
        if stuff.price > self.money:
            return False
        else:
            place = self.determine_place_to_put(stuff)
            if place != NamesStorage.not_found:
                AdditionalFunctions.put_unit_to_place_holder(stuff, place)
                self.money -= stuff.price
                return True

    def determine_place_to_put(self, stuff):
        if stuff.kind in NamesStorage.products_kinds:
            put_to = self.refrigerators_corner[0]
        elif stuff.kind in NamesStorage.techno_kinds:
            put_to = self.refrigerators_corner
        elif stuff.kind in NamesStorage.pet_kinds:
            put_to = self.pets
        else:
            self.voice.nuh.play()
            return NamesStorage.not_found
        if AdditionalFunctions.is_units_holder_full(put_to):
            self.voice.nuh.play()
            return NamesStorage.not_found
        return put_to

    # Mood

    def check_mood(self):
        if self.mood > 80:
            self.step = 7
        elif 30 <= self.mood <= 80:
            self.step = 5
        else:
            self.step = 3

    def full_mood(self):
        self.mood = self.max_mood

    def add_s_mood(self):
        self.mood += self.max_mood * 0.1
        if self.mood > self.max_mood:
            self.mood = self.max_mood

    def add_m_mood(self):
        self.mood += self.max_mood * 0.25
        if self.mood > self.max_mood:
            self.mood = self.max_mood

    def add_l_mood(self):
        self.mood += self.max_mood * 0.4
        if self.mood > self.max_mood:
            self.mood = self.max_mood

    def say_nuh(self):
        self.voice.nuh.play()


class AnimalSeller(Animal):
    def __init__(self, name, hp, kind, x_pos, y_pos, sprites, voice, pets):
        super().__init__(name, hp, kind, x_pos, y_pos, sprites, voice)
        self.pets = UnitStorage('pets', 20, pets)

    def render(self, screen):
        self.set_top_panel_position()
        self.top_panel.render(screen)
        screen.blit(self.bitmap, (self.x, self.y))

    def response(self):
        self.show_price()
        self.show_top_panel()

    def show_price(self):
        for pet in self.pets.units:
            if AdditionalMethods.is_mouse_pos_in_area(pet.area, (pet.x, pet.y)):
                self.top_panel.change_text(str(pet.price) + "$")
                return
            else:
                self.top_panel.change_text("Price")

    def get_pet(self):
        for pet in self.pets.units:
            if AdditionalMethods.is_mouse_pos_in_area(pet.top_panel.area, pet.top_panel.get_position()):

                sold_pet = Cat(pet.name, pet.max_hp + 1, pet.kind, pet.breed, pet.price, pet.x, pet.y,
                               pet.step, pet.sprites, pet.voice)
                if pet.kind == "cat":
                    pass
                else:
                    sold_pet = Dog(pet.name, pet.max_hp + 1, pet.kind, pet.breed, pet.price, pet.x, pet.y,
                                   pet.step, pet.sprites, pet.voice)
                sold_pet.top_panel.change_text('Feed')
                return sold_pet


class Cashier(Animal):
    def __init__(self, name, hp, kind, x_pos, y_pos, sprites, voice, shop_windows):
        super().__init__(name, hp, kind, x_pos, y_pos, sprites, voice)
        self.shop_windows = shop_windows
        self.set_top_panel_position()

    def show_price(self):
        try:
            for shop_window in self.shop_windows:
                unit = shop_window.get_stuff()
                self.top_panel.change_text(str(unit.price) + "$")
                return
            else:
                self.top_panel.change_text("Price")
        except:
            self.top_panel.change_text("Price")

    def render(self, screen):
        self.show_top_panel()
        self.top_panel.render(screen)
        screen.blit(self.bitmap, (self.x, self.y))


class Bitch(Animal):
    def __init__(self, name, hp, kind, x_pos, y_pos, sprites, voice):
        super().__init__(name, hp, kind, x_pos, y_pos, sprites, voice)
        self.max_mood = 30
        self.mood = 0
        self.set_top_panel_position()
        AdditionalMethods.invisible_area(self.hp_panel.area)

    def drink(self):
        self.mood += random.randrange(5, 15)
        if self.mood > self.max_mood:
            self.mood = self.max_mood

    def check_mood(self):
        if self.mood < self.max_mood:
            self.top_panel.change_text('Drink')
        else:
            self.top_panel.change_text('Sex')


class MPCPet(Pet):
    def __init__(self, name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice):
        super().__init__(name, hp, kind, breed, price, x_pos, y_pos, step, sprites, voice)
        self.top_panel.change_text("Buy")

    def render(self, screen):
        self.set_top_panel_position()
        self.top_panel.render(screen)
        screen.blit(self.bitmap, (self.x, self.y))




