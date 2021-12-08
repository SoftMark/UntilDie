import pygame, random, copy
from .values import Values
from .methods import AdditionalMethods
from .rgb import Colors
from .add_functions import AdditionalFunctions
from .storage import NamesStorage
from .display import ChoicePanel
from .values import Values
from .sounds import MoneySounds


class Stuff:
    def __init__(self, price, kind):
        self.price = price
        self.kind = kind


class Talker:
    def __init__(self, sounds):
        self.sounds = sounds

    @classmethod
    def talk(cls, sound):
        sound.play()


class UnitStorage:
    def __init__(self, name, capacity, units):
        self.name = name
        self.capacity = capacity
        self.units = units


class SimpleUnitStorage:
    def __init__(self, capacity, units):
        self.capacity = capacity
        self.units = units


class SeparateStorage(UnitStorage):
    def __init__(self, name, capacity, price, kind, units):
        super().__init__(name, capacity, units)
        self.price = price
        self.kind = kind
        self.units = units


class ShowAbleStorage(SimpleUnitStorage):
    def __init__(self, capacity, units):
        super().__init__(capacity, units)
        self.sectors_in_raw = 4
        self.condition = NamesStorage.closed

    def set_sectors_in_raw(self, sectors_in_raw):
        self.sectors_in_raw = sectors_in_raw

    @classmethod
    def create_sectors_area(cls, size):
        sectors_area = AdditionalMethods.create_panel_area(size)
        return sectors_area

    def create_sectors(self, sectors_area):
        sectors = AdditionalMethods.create_sectors_for_area(sectors_area, self.capacity, self.sectors_in_raw)
        return sectors

    def draw_my_sectors(self, sectors_area, sectors):
        AdditionalMethods.compare_sectors_with_objects(sectors, self.units)
        AdditionalMethods.draw_sectors(sectors_area, sectors)

    def show_units(self, sectors_area):
        self.condition = NamesStorage.opened
        AdditionalMethods.visible_area(sectors_area)

    def hide_units(self, sectors_area):
        self.condition = NamesStorage.closed
        AdditionalMethods.invisible_area(sectors_area)


class RootObject:
    def __init__(self, name, img_file_way):
        self.name = name
        self.bitmap = pygame.image.load(img_file_way)
        self.x = 0
        self.y = 0
        self.area = AdditionalMethods.create_panel_area(self.bitmap.get_size())
        # Add bitmap to area
        self.area.blit(self.bitmap, (0, 0))
        self.area.set_colorkey(Colors.snow)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def render(self, screen):
        screen.blit(self.area, (self.x, self.y))

    def set_position(self, position):
        self.set_x(position[0])
        self.set_y(position[1])

    def get_position(self):
        position = (self.x, self.y)
        return position

    def get_height(self):
        return self.area.get_height()

    def get_width(self):
        return self.area.get_width()


class StaticRootObject(RootObject):
    def __init__(self, name, img_file_way, position):
        super().__init__(name, img_file_way)
        self.set_position(position)


class TopPanelCarrierObject(RootObject):
    def __init__(self, name, img_file_way, top_panel_text):
        super().__init__(name, img_file_way)
        self.top_panel = ChoicePanel(top_panel_text, Colors.black, Colors.black, (0, 0))
        self.top_panel_distance = 20
        self.top_panel_condition = NamesStorage.closed
        self.set_top_panel_position()
        self.top_panel.invisible()

    def set_top_panel_position(self):
        self.top_panel.x = self.x + AdditionalFunctions.minus_half(self.bitmap.get_width(),
                                                                   self.top_panel.area.get_width())
        self.top_panel.y = self.y - self.top_panel_distance - self.top_panel.area.get_height()
        self.top_panel.position = (self.top_panel.x, self.top_panel.y)

    def render(self, screen):
        self.top_panel.render(screen)
        screen.blit(self.area, (self.x, self.y))

    def show_top_panel(self):
        self.top_panel_condition = NamesStorage.opened
        self.top_panel.visible()

    def hide_top_panel(self):
        self.top_panel_condition = NamesStorage.closed
        self.top_panel.invisible()

    def response(self):
        self.show_top_panel()

    def sleep(self):
        self.hide_top_panel()


class WorkDesk(TopPanelCarrierObject):
    def __init__(self, name, img_file_way, top_panel):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel)
        self.default_position = (Values.room_width - 3 * Values.wall_width // 2 - self.area.get_width()
                                 , Values.room_height - Values.floor_height - 4 * self.area.get_height() // 5 )
        self.set_position(self.default_position)
        self.set_top_panel_position()

    def render(self, screen):
        self.top_panel.render(screen)
        screen.blit(self.bitmap, self.get_position())


class Door(TopPanelCarrierObject, Stuff, Talker):
    def __init__(self, name, img_file_way, top_panel, price, kind, sounds):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel)
        Stuff.__init__(self, price, kind)
        Talker.__init__(self, sounds)
        # Position
        self.default_position = (Values.wall_width * 2, Values.room_height - Values.floor_height
                                 - self.bitmap.get_height())
        self.set_position(self.default_position)
        self.set_top_panel_position()


class Refrigerator(ShowAbleStorage, TopPanelCarrierObject, Talker, Stuff):
    def __init__(self, name, capacity, price, kind, units, img_file_way, top_panel, sounds):
        ShowAbleStorage.__init__(self, capacity, units)
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel)
        Talker.__init__(self, sounds)
        Stuff.__init__(self, price, kind)
        # Position
        self.default_position = (Values.room_width - 3 * Values.wall_width // 2, Values.room_height
                                 - Values.floor_height - 4 * self.bitmap.get_height() // 5)
        self.set_position(self.default_position)
        self.set_top_panel_position()
        # Sectors
        self.products_panel = self.create_sectors_area(self.bitmap.get_size())
        self.sectors = self.create_sectors(self.products_panel)
        self.hide_units(self.products_panel)
        self.condition = NamesStorage.closed

    def render(self, screen):
        AdditionalMethods.clear_area(self.area)
        AdditionalMethods.put_on_area(self.area, self.bitmap, self.products_panel)
        self.top_panel.render(screen)
        screen.blit(self.area, self.get_position())

    def response(self):
        self.show_top_panel()
        AdditionalMethods.compare_sectors_with_objects(self.sectors, self.units)
        AdditionalMethods.draw_sectors(self.products_panel, self.sectors)
        if not AdditionalFunctions.is_place_holder_empty(self) and self.condition == NamesStorage.opened:
            AdditionalMethods.check_sectors_response(self.sectors, self.get_position())

    def sleep(self):
        if self.top_panel_condition == NamesStorage.opened:
            self.hide_top_panel()
        if self.condition == NamesStorage.opened:
            self.get_closed()

    def get_opened(self):
        self.condition = NamesStorage.opened
        self.show_units(self.products_panel)
        self.top_panel.change_text('Close')
        self.sounds.open.play()

    def get_closed(self):
        self.condition = NamesStorage.closed
        self.hide_units(self.products_panel)
        self.top_panel.change_text('Open')
        self.sounds.close.play()

    def get_product(self):
        index = AdditionalMethods.get_chose_object_index(self.sectors, self.get_position())
        product = self.units[index]
        del self.units[index]
        return product

    def change_condition(self):
        if self.condition == NamesStorage.closed:
            self.get_opened()
        elif self.condition == NamesStorage.opened:
            self.get_closed()


class Product:
    def __init__(self, name, hp, price, kind, img_file_name):
        self.name = name
        self.hp = hp
        self.price = price
        self.kind = kind
        dict_for = {'human': True, 'dog': True, 'cat': True}
        if self.kind == 'sea-food':
            dict_for['dog'] = False
        elif self.kind in ['vegetable', 'fruit', 'alcohol-drink', 'sweet-drink']:
            dict_for['dog'] = False
            dict_for['cat'] = False
        self.for_human = dict_for['human']
        self.for_dog = dict_for['dog']
        self.for_cat = dict_for['cat']
        self.bitmap = pygame.image.load('images/products/' + img_file_name + '.png')
        self.area = AdditionalMethods.create_panel_area(self.bitmap.get_size())
        # Add bitmap to area
        self.area.blit(self.bitmap, (0, 0))
        self.area.set_colorkey(Colors.snow)

    def render(self, screen, position):
        screen.blit(self.bitmap, position)


class Place:
    def __init__(self, name, img_file_name):
        self.name = name
        self.bitmap = pygame.image.load(img_file_name)

    def render(self, screen, position):
        screen.blit(self.bitmap, position)


class ShopWindow(ShowAbleStorage, TopPanelCarrierObject, Talker):
    def __init__(self, name, capacity, units, img_file_way, top_panel, sounds):
        ShowAbleStorage.__init__(self, capacity, units)
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel)
        Talker.__init__(self, sounds)
        self.sectors_in_raw = 3
        # Position
        self.default_position = (Values.room_width - 2.5 * Values.wall_width - self.bitmap.get_width(),
                                 Values.room_height - Values.floor_height - self.bitmap.get_height() + 10)
        self.set_position(self.default_position)
        self.set_top_panel_position()
        # Sectors
        self.stuff_panel = self.create_sectors_area(self.bitmap.get_size())
        self.sectors = self.create_sectors(self.stuff_panel)
        self.hide_units(self.stuff_panel)
        self.condition = NamesStorage.closed

    def render(self, screen):
        AdditionalMethods.clear_area(self.area)
        AdditionalMethods.put_on_area(self.area, self.bitmap, self.stuff_panel)
        self.top_panel.render(screen)
        screen.blit(self.area, self.get_position())

    def response(self):
        self.show_top_panel()
        self.get_opened()
        self.show_stuff_nutritional_value()
        AdditionalMethods.check_sectors_response(self.sectors, self.get_position())
        AdditionalMethods.compare_sectors_with_objects(self.sectors, self.units)
        AdditionalMethods.draw_sectors(self.stuff_panel, self.sectors)

    def sleep(self):
        if self.top_panel_condition == NamesStorage.opened:
            self.hide_top_panel()
        if self.condition == NamesStorage.opened:
            self.get_closed()

    def get_opened(self):
        self.condition = NamesStorage.opened
        self.show_units(self.stuff_panel)

    def get_closed(self):
        self.condition = NamesStorage.closed
        self.hide_units(self.stuff_panel)

    def get_stuff(self):
        if self.condition == NamesStorage.opened:
            index = AdditionalMethods.get_chose_object_index(self.sectors, self.get_position())
            product = self.units[index]
            return product

    def show_stuff_price(self):
        try:
            index = AdditionalMethods.get_chose_object_index(self.sectors, self.get_position())
            self.top_panel.change_text(str(self.units[index].price) + "$")
        except:
            self.top_panel.change_text("Price")

    def show_stuff_nutritional_value(self):
        try:
            index = AdditionalMethods.get_chose_object_index(self.sectors, self.get_position())
            self.top_panel.change_text(str(self.units[index].hp) + "hp")
        except:
            self.top_panel.change_text("Health")


class Inventory(RootObject, ShowAbleStorage):
    def __init__(self, name, capacity, units, img_file_way):
        RootObject.__init__(self, name, img_file_way)
        ShowAbleStorage.__init__(self, capacity, units)
        # Position
        self.default_position = (0, 0)
        self.set_position(self.default_position)
        # Sectors
        self.stuff_panel = self.create_sectors_area(self.bitmap.get_size())
        self.sectors = self.create_sectors(self.stuff_panel)
        self.hide_units(self.stuff_panel)
        self.condition = NamesStorage.closed

    def render(self, screen):
        AdditionalMethods.clear_area(self.area)
        AdditionalMethods.put_on_area(self.area, self.bitmap, self.stuff_panel)
        screen.blit(self.area, self.get_position())

    def response(self):
        AdditionalMethods.check_sectors_response(self.sectors, self.get_position())
        AdditionalMethods.compare_sectors_with_objects(self.sectors, self.units)
        AdditionalMethods.draw_sectors(self.stuff_panel, self.sectors)

    def sleep(self):
        if self.condition == NamesStorage.opened:
            self.get_closed()

    def get_opened(self):
        self.condition = NamesStorage.opened
        self.show_units(self.stuff_panel)

    def get_closed(self):
        self.condition = NamesStorage.closed
        self.hide_units(self.stuff_panel)

    def get_stuff(self):
        index = AdditionalMethods.get_chose_object_index(self.sectors, self.get_position())
        product = self.units[index]
        del self.units[index]
        return product

    def change_condition(self):
        if self.condition == NamesStorage.closed:
            self.get_opened()
        elif self.condition == NamesStorage.opened:
            self.get_closed()


class Bar(TopPanelCarrierObject):
    def __init__(self, name, img_file_way, top_panel_text, alcohol):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel_text)
        self.set_x(Values.room_width - self.area.get_width())
        self.set_y(Values.room_height - self.area.get_height())
        self.set_top_panel_position()
        self.alcohol = alcohol

    def generate_alcohol(self):
        return self.alcohol[random.randrange(0, len(self.alcohol))]


class CoffeeMachine(TopPanelCarrierObject, Talker):
    def __init__(self, name, img_file_way, top_panel_text, sounds):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel_text)
        Talker.__init__(self, sounds)
        #self.set_x(Values.wall_width + self.area.get_width() // 4)
        self.set_x(3.5 * Values.wall_width)
        self.set_y(Values.room_height - self.area.get_height() - Values.floor_height)
        self.set_top_panel_position()
        self.coffee_price = 2


class FootballTable(TopPanelCarrierObject, Talker):
    def __init__(self, name, img_file_way, top_panel_text, sounds):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel_text)
        Talker.__init__(self, sounds)
        self.set_x(Values.wall_width // 2)
        self.set_y(Values.room_height - self.area.get_height() - Values.floor_height // 4)
        self.set_top_panel_position()


class Armchair(TopPanelCarrierObject):
    def __init__(self, name, img_file_way, top_panel_text):
        TopPanelCarrierObject.__init__(self, name, img_file_way, top_panel_text)
        self.set_position((int(0.5 * Values.wall_width), int(3.5 * Values.floor_height)))
        self.set_top_panel_position()

    def heal(self, player, FPS):
        hunger_damage = 1 / FPS * 2 / 500
        if AdditionalMethods.is_in_response_range(self, player):
            if player.hp < player.max_hp:
                player.hp += 1.2 * player.max_hp * hunger_damage

        if player.hp >= player.max_hp:
            player.hp = player.max_hp - 1


class Window:
    def __init__(self):
        self.x = Values.wall_width * 3.2
        self.y = Values.roof_height * 2.3
        self.day_sprite = pygame.image.load("images/window_day.png")
        self.night_sprite = pygame.image.load("images/window_night.png")
        self.bitmap = self.night_sprite
        self.area = AdditionalMethods.create_panel_area(self.bitmap.get_size())
        # Add bitmap to area
        self.area.blit(self.bitmap, (0, 0))
        self.area.set_colorkey(Colors.snow)

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

    def check_time(self, clock):
        if 6 <= clock.hours <= 22:
            self.bitmap = self.day_sprite
        else:
            self.bitmap = self.night_sprite


class FloatingCoin():
    sounds = MoneySounds()

    def __init__(self):
        self.bitmap = pygame.image.load("images/money.png")
        self.area = AdditionalMethods.create_panel_area(self.bitmap.get_size())
        # Add bitmap to area
        self.area.blit(self.bitmap, (0, 0))
        self.area.set_colorkey(Colors.snow)
        self.x = 0
        self.y = 0
        self.life_damage = random.randrange(1, 5)
        self.is_active = False
        self.value = None
        self.alpha = 255

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def render(self, screen):
        if self.is_active:
            screen.blit(self.area, (self.x, self.y))

    def set_position(self, position):
        self.set_x(position[0])
        self.set_y(position[1])

    def get_position(self):
        position = (self.x, self.y)
        return position

    def invisible(self):
        if self.is_active:
            self.alpha -= self.life_damage
        self.area.set_alpha(self.alpha)

    def generate_position(self):
        self.set_x(random.randrange(0, Values.room_width - self.area.get_width()))
        self.set_y(random.randrange(0, Values.room_height - self.area.get_height()))

    def generate_value(self):
        self.value = random.randrange(1, 5)

    def generate(self):
        if not self.is_active:
            self.is_active = True
            self.generate_position()
            self.generate_value()
            self.area.set_alpha(self.alpha)
            return 1
        
        return 0


class DollarGun:
    MAX_COINS = 5

    def __init__(self):
        self.coins = [FloatingCoin() for i in range(random.randrange(1, self.MAX_COINS))]
        self.coins_active = 0
        self.current_dollars = self.coins
        self.sleep_time = 1
        self.secs = 0

    def generate_sleep_time(self):
        self.sleep_time = random.randrange(2, 7)

    def sleep(self):
        pass

    def run(self, screen, FPS):
        if len(self.current_dollars) <= 3:
            self.coins.extend([FloatingCoin() for i in range(random.randrange(1, self.MAX_COINS))])

        for current_dollar in self.current_dollars:
            if AdditionalFunctions.rand_bool(0.2) and self.coins_active < self.MAX_COINS:
                self.coins_active += current_dollar.generate()

        count_delete = 0
        for i in range(len(self.current_dollars)):
            i -= count_delete
            self.current_dollars[i].render(screen)
            self.current_dollars[i].invisible()
            if self.current_dollars[i].area.get_alpha() <= 0:
                count_delete += 1
                self.coins_active -= 1
                del self.current_dollars[i]

    def drop_money(self, number):
        self.coins[number].sounds.dropping.play()
        self.coins_active -= 1
        del self.current_dollars[number]
        if not self.current_dollars:
            self.generate_sleep_time()

